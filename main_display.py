from teacher import Teacher
from student import Student
from grade import Grade
from load import Load

print()
print('Student')
student1 = Student('00-0001','Manganaan', 'John Lloyd', 'Barliso', 'Student', '1', 'BSCS', 'A')
print(student1.getName())
print(student1.getYrCrseSec())
print(student1)

print()
print('Grade')
grade1 = Grade(99, 78, 85, 90)
grade1.id = '001'
grade1.last_name = 'Manganaan'
grade1.first_name = 'John Lloyd'
grade1.middle_name = 'Barliso'
grade1.course = 'BSCS'
grade1.year = 1
grade1.section = 'A'
print(grade1.getName())
print(grade1.getYrCrseSec())
print(grade1.getAverage())

print()
print('Teacher')
teacher1 = Teacher('01-0000', 'Manganaan', 'John Lloyd', 'Barliso', 'Teacher', 'CEIT', 'Instructor')
print(teacher1.getDepartment())
print(teacher1.getName())
print(teacher1)


print()
print('Load')
load_1 = Load('Architecture and Organization', 'System Fundamentals', 'Networks and Communications')
load_1.id = '001'
load_1.last_name = 'Manganaan'
load_1.first_name = 'John Lloyd'
load_1.middle_name = 'Barliso'
load_1.department = 'Ceit'
load_1.position = 'Instructor'
print(load_1.getName())
print(load_1.getDepartment())
print(load_1.getPosition())
print(load_1.getLoad())




