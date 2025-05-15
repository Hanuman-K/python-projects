from array import *
from numpy import *
#array
a=array([1,2,3,4])
print(a*2)
print('%.2f' %a[0]) #Format this number as a float, rounded to 2 decimal places
ar=array([1,2,3,4,5],float)
print(ar)
print(ar.dtype)

arr=array([1,2,3,4])
print(arr)
print(arr.dtype)

#linspace
arr1=linspace(0,10,5)
print(arr1)
arr2=linspace(1,50)
print(arr2)

#arrange
arr3=arange(3,14,2)
print(arr3)
arr4=arange(3,14)
print(arr4)

#logspace
arr5=logspace(2,10,10)
print(arr5)
print(arr5[0])

print('%.2f' %arr5[0])

#zeros
arr6=zeros(5)
print(arr6)

arr6=zeros(5,int)
print(arr6)

#ones
arr7=ones(5)
print(arr7)
arr7=ones(5,int)
print(arr7)
