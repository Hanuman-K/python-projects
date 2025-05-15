
class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollmo=rollno
        self.lap=self.laptop()  #we are mentioning inner class here so that it helps in easy callling
    def show(self):
        print(self.name,self.rollmo)
        self.lap.show()    #we are using lap because its variable mentioned in outerclass already
    class laptop:          #we can create this in outside the outer class but only stdents can have laptop then inside
        def __init__(self):
            self.brand="hp"
            self.cpu="i5"
            self.ram="1tb"
        def show(self):
            print(self.brand,self.cpu,self.ram)
s1=student("navin",2)
s2=student("harry",3)
s1.show()
s2.show()
a=s1.lap.brand,s1.lap.cpu,s1.lap.ram
print(a)
lap1=student.laptop()
print(lap1)