def greet():
    print('helo')
    print('good morning')
greet()


def plus_minus(a,b):
    x=a+b
    y=a-b
    return x,y
print(plus_minus(8,6))

def add_sub(a,b):
    x=a+b
    y=a-b
    print(x)
    print(y)
add_sub(3,2)


def update(x):
    print(id(x) ,1)
    x=8
    print(id(x) ,2)
    print('x' ,x)

a=10
print(id(a) ,3)
update(a)
print(id(a) ,4)
print('a' ,a)


def person(name,age):  #formal argument (everything inside this is argument)
    print(name)
    print(age)

person('hanuman',25) #when we use its actual argument and in this case its #position

person(age=25,name='hanuman') #keyword

def person1(name,age=18):
    print(name)
    print(age)

person1('hanuman') #default i didnt enter age but in formal its already mentioned


def sum(a,*b):  #variable length argument
    c=a
    for i in b:
        c=c+i
    print('addition of a+b :',c)

sum(1,2,3,4,5) # variable length argument


def sum(*b):  #variable length argument
    c=0
    for i in b:
        c=c+i
    print('addition of all :',c)

sum(1,2,3,4,5) # variable length argument



def human(name,*data):  #variable length argmenent
    print(name)
    print(data)

human('hanuman',32,'hyd','243546')

def human1(name,**data):  #keyword variable length argmenent
    print(name)
    print(data)

human1('hanuman',age=27,city='hyd',mob='243546')

def human2(name,**data):  #keyword variable length argmenent
    print(name)
    for i,j in data.items():
        print(i,j)

human2('hanuman',age=27,city='hyd',mob='243546')

