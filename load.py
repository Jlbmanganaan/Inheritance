from teacher import Teacher

class Load(Teacher):
    def __init__(self, load1, load2, load3) -> None:
        self.load1 = load1
        self.load2 = load2
        self.load3 = load3

    def getLoad(self):
        return f'{self.load1} | {self.load2} | {self.load3}'
    