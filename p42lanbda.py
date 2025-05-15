from functools import reduce


def sqr(a):
    return a*a

a=sqr(2)
print(a)

#we can use lamda instad of wasting two lines for def and return
f=lambda a:a*a
res=f(5)
print(res)

h=lambda b,c:b+c
ans=h(5,3)
print(ans)

#filter
def is_even(n):
    return n%2==0
no=[1,23,4,55,94,86]
sol=list(filter(is_even,no))
print(sol)

evens=list(filter(lambda n:n%2==0,no)) #by using lambda
print(evens)
doubles=list(map(lambda n:n*2,evens))
print(doubles)
sum=reduce(lambda a,b:a+b,doubles)   #we have to import reduce from functools
print(sum)




