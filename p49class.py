class computer:
    def hanu(self):
        print("good",27,"5inch")
com=computer()
computer.hanu(com)
#or
com.hanu()

print(type(com))
a=8
print(type(a))
name="sonu"
print(type(name))

class telvadhu:               #class
    def __init__(self):              #specal_method
        print("init")

    def hole(self):                      #method
        print("print: ")
check1=telvadhu()    #  telvadhu() is constructor
check2=telvadhu()   #object

check1.hole()    #we called only once but splmethod calls two times becasuse for every object it calls

class telusko:
    def __init__(self,k,h):   #(,,)what ever writeen in it is argument
        self.kitchen=k
        self.hall=h
    def home(self):
        print("intlo :",self.kitchen,self.hall)

tel=telusko("poyi","thinta")
chep=telusko("kuralu","panta")

tel.home()
chep.home()

#we cant print directly c1=computer()/print(id(c1)) we have to write class for it
#even though if write class the object will be called only by __init__ method
class computer1:
    pass
c1=computer1()
print(id(c1))   #the size willbe given by constructor


#self
class solo:
    def __init__(self):
        self.name="ko"
        self.age=23
    def nuve(self):
        self.name="ki"

a=solo()
b=solo()

print(a.name)
print(b.name)

a.name="ok"
print(a.name)

a.nuve()
print(a.name)

#compare
class polika:
    def acham(self):
        self.name="name"
    def chudu(self):
        self.name1="name"
    def compare(self,other):
        if self.name==other.name1:
            print("both are same")
        else:
            print("both are not same")
a=polika()
a.acham()
print(a.name)
b=polika()
b.chudu()
print(b.name1)
a.compare(b)

#class variable,instance variable
class car:
    wheels = 4
    def __init__(self):
        self.name="bmw"
        self.model="mor"
c1=car()
c2=car()
c1.name="audi"
print(c1.name,c1.model,c1.wheels)
print(c2.name,c2.model,c2.wheels)



