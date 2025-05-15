

from array import *
a=array('i',[])
x=int(input("enter the length of val: "))
for i in range(x):
    v=int(input("enter the value: "))
    a.append(v)
print(a)

m=int(input("enter the value to search: "))
k=0
for j in a:
    if j==m:
        print(k)
        break
    k+=1

from operator import index
print(a.index(m))