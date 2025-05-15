#adding two multi dimenarray is called

from array import *
from numpy import *

a1=array([1,2,3,4])
a2=array([5,6,7,8])
a3=a1+a2
print(a3)

print(concatenate([a1,a2]) ,1)
print(log(a1) ,2)
print(sqrt(a1) ,3)
print(sin(a1) ,4)
print(cos(a1) ,5)
print(sort(a1) ,6)
print(sum(a1) ,7)
print(min(a1) ,8)
print(max(a1) ,9)

arr1=array([1,2,3,4])
arr2=arr1
print(arr1)
print(id(arr1))
print(arr2)
print(id(arr2))
arr2=arr1.view()  #for diff id
print(arr2)
print(id(arr2))


ar1=array([2,6,8])
print(id(ar1))
ar2=ar1.copy()
ar1[1]=7
print(ar1)
print(ar2)
print(id(ar1))
print(id(ar2))

ar1=array([2,6,8])
ar2=ar1.view()
ar1[1]=9
print(ar1)
print(ar2)
print(id(ar1))
print(id(ar2))

