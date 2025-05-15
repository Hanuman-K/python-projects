#multiple inheritance
class A:
    def feature1(self):
        print("feature1 is working")
    def feature2(self):
        print("feature2 is working")
class B:
    def feature3(self):
        print("feature3 is working")
    def feature4(self):
        print("feature4 is working")
class c(B,A):
    def feature5(self):
        print("feature1 is working")
    def feature6(self):
        print("feature6 is working")
c1=c()
c1.feature1()

#multi level inheritance
class A:
    def feature1(self):
        print("feature1 is working")
    def feature2(self):
        print("feature2 is working")
class B(A):
    def feature3(self):
        print("feature3 is working")
    def feature4(self):
        print("feature4 is working")
class c(B):
    def feature5(self):
        print("feature1 is working")
    def feature6(self):
        print("feature6 is working")
c1=c()
c1.feature2()

#single level inherance
class A:
    def feature1(self):
        print("feature1 is working")
    def feature2(self):
        print("feature2 is working")
class B(A):
    def feature3(self):
        print("feature3 is working")
    def feature4(self):
        print("feature4 is working")

b1=B()
b1.feature1()

#constructor in inheritance
#case1
class A:
    def __init__(self):
        print("init A","case1")
    def feature1(self):
        print("feature 1a working")
class B(A):
    def feature2(self):
        print("feature 1b working")
a1=B()

#case 2
class A:
    def __init__(self):
        print("init A")
    def feature1(self):
        print("feature 1a working")
class B(A):
    def __init__(self):
        print("init B","case 2")
    def feature2(self):
        print("feature 1b working")
a1=B()

#case 3
class A:
    def __init__(self):
        print("init A","case3")
    def feature1(self):
        print("feature 1a working")
class B(A):
    def __init__(self):
        super().__init__()
        print("init B","case 3")
    def feature2(self):
        print("feature 1b working")
a1=B()

#case4
class A:
    def __init__(self):
        print("init A","case4")
    def feature1(self):
        print("feature 1a working")
class B:
    def __init__(self):   #if u write super()...here,then we get b()init in o/p
        print("init B","case4")
    def feature2(self):
        print("feature 1b working")
class C(B,A):   #only C(----,)in first place that init is accesable in output
    def __init__(self):
        super().__init__()
        print("init C","case4")
a1=C()
