#if user gives input and without using __init__
class student:
    def marks(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

a=student()
a.marks(1,2,3)
print(a.m1)
print(a.m2)
print(a.m3)

#if we use __init__ and self user gives input
class student1:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

a=student1(1,2,3)
print(a.m1)
print(a.m2)
print(a.m3)

class student2:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

a=student2(1,2,3 )

print(a.avg())
print(a.m1)
print(a.m2)
print(a.m3)

#methods
class student3:
    school="telusko"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod       #decorator for class method
    def getclass(cls):                #we have to use cls in classmethod instead of self
        return cls.school              #we have to use cls.(classvariable)
    @staticmethod        #decorator for staticmethod
    def info():         #we need to write(self or cls) in brackets only when we need to call object or class
        print("this is staticmethod")
s1=student3(1,2,3)
print(s1.avg())
print(student3.getclass())         #for classmethod we have to call class.classMethodName
student3.info()        #in static method we have to use class when calling


