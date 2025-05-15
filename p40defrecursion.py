#recurrsion

import sys
print(sys.getrecursionlimit())    #to check the recursion limit
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

i=0
def greet():
    global i
    i+=1
    print("hello",i)
    #greet()           #unhash this for further use
                                      #function is calling itself in function
greet()  #it will call for 2000 times as we increased from 1000 to 2000



#factoral with recursion

def fact(n):
    if n==0:
        return 1
    return n* fact(n-1)
result = fact(5)
print(result)

