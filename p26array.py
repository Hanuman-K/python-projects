from array import *
val=array('i',[2,6,-7,5,86])
print(val)

val2=array('I',[2,6,7,5,86])
print(val2)

val3=array('f',[2,6,-7,5,86])
print(val3)

#gives the size of the array
val4=array('i',[2,6,-7,5,86])
print(val4.buffer_info()) #(adresss,count)

val5=array('l',[2,6,-7,5,86])
print(val5.typecode)

val6=array('i',[2,6,-7,5,86])
val6.append(54)
print(val6)
val6.reverse()
print(val6)
val6=array('i',sorted(val6))
print(val6)
val6.reverse()
print(val6)

for i in val6:
    print(i)

vl=array('u',['h','d','l','e','o'])
for i in vl:
    print(i)

v=array('i',[2,6,-7,5,86])
nv=array(v.typecode,(a for a in v))
print(nv)

i=0
while i<len(nv):
    print(nv[i])
    i+=1