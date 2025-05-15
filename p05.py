no=[23,54,76,12,54]
print(no)
print(no[3])
name=['sonu','monu','tonu']
print(name)
print(name[1])
print([no,name])
no.append(45)
print(no)

no.insert(2,77)
print(no)

no.remove(12)
print(no)

no.pop(2) #almost like remove
print(no,1)

no.pop() #last addedone will be removed
print(no)

del no[2:]
print(no)

no.extend([25,34,567,8,84]) #to add a list
print(no)

print(min(no))
print(max(no))
print(sum(no))

no.sort()
print(no)

no.sort(reverse=True)
print(no)

l=[('p1',21),('p4',24),('p3',15),('p2',30)]
print(l)
def x(y):
    return y[0] #from (p1,21) choosing p1,if y[1] then 21
l.sort(key=x)
print(l)


print(type(name))
a='hanu'
print(type(a))
print(type(no))

