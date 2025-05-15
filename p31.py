from array import *
from numpy import *
a1=array([[1,2,3],
          [4,5,6]])
print(a1)
print(a1.dtype)
print(a1.ndim) #no. of dimenstions i.e,[[hw many we use KIND]]
print(a1.shape)
print(a1.size)

a2=a1.flatten()
print(a2)

aa1=array([[1,2,3,4,5,6,7,8],
           [8,7,6,5,4,3,2,1]])
aa2=aa1.reshape(4,4)
print(aa2)

aa3=aa1.reshape(2,4,2)
print(aa3)

m=matrix('1,2,3;4,5,6;7,8,9')
print(diagonal(m))
print(m.min())
print(m.max())
m1=matrix('1,2,3;4,5,6;7,8,9')
m3=m1*m
print(m3)

