class Student:
    school = "DAV"
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.__private = "Private"
        self._protected = "Protected"

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def getSchoolName(cls):
        return cls.school

    # Nothing to do with class or instance
    @staticmethod
    def info():
        print("This is Student class in abc module")

a = Student(1,2,3)
print(a.avg())
print(Student.getSchoolName())
Student.info()
print(a._protected)
print(a.__private)

