#ducktyping
from enum import nonmember


class pycharm:
    def exe(self):
        print("compling")
class editor:
    def exe(self):
        print("spell check")
class laptop:
    def code(self,id):
        id.exe()
id=pycharm()
lap=laptop()
lap.code(id)
#0r instead class for laptop if we write directly function for laptop and execte
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm pretending to be a duck!")

def make_it_quack(thing):
    thing.quack()  # No type checking

du = Duck()
per = Person()

make_it_quack(du)    # Quack!
make_it_quack(per)  # I'm pretending to be a duck!



#opertaor overloading
#simple example
a=1
b=2
print(a+b)
print(int.__add__(a,b))

c="hi"
d="5"
print(c+d)
print(str.__add__(c,d))
#here we are overloading the __add__ method(whixh is operator) acc to over convient
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self, other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s=student(m1,m2)
        return s
    def __str__(self):   #see this in second one alos and check the differnece
        return self.m1,self.m2
s1=student(2,3)
s2=student(4,5)
s=s1+s2
print(s.m1,s.m2)
print(s1.__str__())


class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __gt__(self, other):
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        s=student(r1,r2)
        if r1>r2:
            return True
        else:
            return False
    def __str__(self):    #from above code str,see the difference
        return '{},{}'.format(self.m1,self.m2)

s1=student(5,3)
s2=student(1,8)
if s1>s2:
    print("s1 wins")
else:
    print("s2 wins")
a=9
print(a)
print(a.__str__())
print(s1.__str__())
print(s2)


#method overloading
class student:
    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s
s1=student()
print(s1.sum(1))
print(s1.sum(1,1))
print(s1.sum(1,1,1))
#other method
class MathOps:
    def add(self, *args):
        return sum(args)

m = MathOps()
print(m.add(2, 3))          # 5
print(m.add(1, 2, 3, 4))    # 10
#another method
from functools import singledispatch

@singledispatch
def process(value):
    print("General case")

@process.register
def _(value: int):
    print("Integer:", value)

@process.register
def _(value: str):
    print("String:", value)

process(10)       # Integer: 10
process("hi")     # String: hi
process(3.14)     # General case

#method overriding

      #example is inheritance
