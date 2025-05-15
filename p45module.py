def cal(a,b):
    def add():
        print(a+b)
    def sub():
        print(a-b)
    def mul():
        print(a*b)
    add()
    sub()
    mul()

print("hello"+ __name__)  #if we use this module we get hellop45module as its the module name but here we get main
def helo():
    print("hi")
    print("hello")
    print(__name__)

if __name__== "__main__":  #if we are not calling helo() by using if
    helo()                 #condition then this helo() output will print when we use this file as a module



