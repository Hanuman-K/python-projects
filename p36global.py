a=10
def something():
    a=15
    print('inside ',a)
something()
print('outside ',a)

#case2
b=5
def some():
    print('in :',b)
some()
print("out: ",b)

#case3
c=10
def someglo():
    global c
    c=7
    print("inside: ",c)
someglo()
print("outside: ",c)

#case4 global and local in same function
d=8      #even though we use def globals d for out  but we have to write it
def gloc():
    d=9
    x=globals()['d']
    print("in:" ,d )
    globals()['d']=15
    print("check:",d)
gloc()
print("out: ",d)


