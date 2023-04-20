from grade import Grade
from load import Load

students = []
teachers = []

def addStudents():
    while True:
        print()
        id = input('Enter id: ')
        lastName = input('Enter Last name: ')
        firstName = input('Enter First name: ')
        middleName = input('Enter Middle name: ')
        year = input('Enter Year: ')
        course = input('Enter Course: ')
        section = input('Enter Section: ')
        print('----------------------------')
        filipino = input('Grade Filipino: ')
        math = input('Grade Math: ')
        science = input('Grade Science: ')
        english = input('Grade English: ')

        stud = Grade(filipino, math, science, english)
        stud.id = id
        stud.last_name = lastName
        stud.first_name = firstName
        stud.middle_name = middleName
        stud.year = year
        stud.course = course
        stud.section = section

        students.append(stud)

        print()
        ans = input('Enter another? [y/n]: ')

        if (ans != 'y'):
            break

    menu()

def deleteStudent():
    i = int(input('Enter index: '))
    students.pop(i)

    menu()

def searchStudent():
    i = int(input('Enter index: '))
    print(f'{i} \t {students[i].getName()} \t | {students[i].getYrCrseSec()} \t | {students[i].getAverage()}')

    menu()

def displayStudent():
    print()
    print('-------------------------------------------------------------------------------')
    i = 0
    for s in students:
        print(f'{i} \t | {s.getName()} \t | {s.getYrCrseSec()} \t | {s.getAverage()}')
        i += 1
    print('-------------------------------------------------------------------------------')

    menu()

def addTeachers():
    while True:
        print()
        id = input('Enter id: ')
        lastName = input('Enter Last name: ')
        firstName = input('Enter First name: ')
        middleName = input('Enter Middle name: ')
        deparment = input('Enter Department: ')
        position = input('Enter Position: ')
        print('----------------------------')
        load1 = input('Grade Load 1: ')
        load2 = input('Grade Load 2: ')
        load3 = input('Grade Load 3: ')

        teach = Load(load1, load2, load3,)
        teach.id = id
        teach.last_name = lastName
        teach.first_name = firstName
        teach.middle_name = middleName
        teach.department = deparment
        teach.position = position


        teachers.append(teach)

        print()
        ans = input('Enter another? [y/n]: ')

        if (ans != 'y'):
            break

    menu()

def deleteTeacher():
    i = int(input('Enter index: '))
    teachers.pop(i)

    menu()

def searchTeacher():
    i = int(input('Enter index: '))
    print(f'{i} \t {teachers[i].getName()} \t | {teachers[i].getDepartment()} \t |  {teachers[i].getPosition()} \t | {teachers[i].getLoad()}')

    menu()

def displayTeacher():
    print()
    print('-------------------------------------------------------------------------------')
    i = 0
    for t in teachers:
        print(f'{i} \t | {t.getName()} \t | {t.getDepartment()} \t | {teachers[i].getPosition()} \t | {t.getLoad()}')
        i += 1
    print('-------------------------------------------------------------------------------')

    menu()

def displayAll():
    print()
    print('---------------------------------------------------------------------------------------------------------')
    print('Student')
    i = 0
    for s in students:
        print(f'{i} \t | {s.getName()} \t | {s.getYrCrseSec()} \t | {s.getAverage()}')
        i += 1

    print()
    print('---------------------------------------------------------------------------------------------------------')
    print('Techer')
    i = 0
    for t in teachers:
        print(f'{i} \t | {t.getName()} \t | {t.getDepartment()} \t | {teachers[i].getPosition()} \t | {t.getLoad()}')
        i += 1
    print('---------------------------------------------------------------------------------------------------------')

    menu()

def deleteAll():
    choice = input('Do you wish to get rid of all the record? [y/n]:' )
    if (choice == 'y'):
        students.pop()
        teachers.pop()
    elif(choice == 'n'):
        print()
        print('Okay perhaps another time')
    
    menu()


def menu():
    print()
    print()
    print('::Menu::')
    print('D - delete Student       S - search Student')
    print('A - add Student          M - display Student')
    print('F - add Teacher          N - display Teacher')
    print('G - delete Teacher       X - display all')
    print('C - search Teacher       Z - delete all')
    print()
    choice = input('Enter a function: ')
    if (choice == 'D'):
        deleteStudent()
    elif (choice == 'A'):
        addStudents()
    elif(choice == 'S'):
        searchStudent()
    elif (choice == 'M'):
        displayStudent()
    elif (choice == 'F'):
        addTeachers()
    elif (choice == 'G'):
        deleteTeacher()
    elif (choice == 'N'):
        displayTeacher()
    elif (choice == 'C'):
        searchTeacher()
    elif(choice == 'X'):
        displayAll()
    elif(choice == 'Z'):
        deleteAll()
    
    print()

menu()

