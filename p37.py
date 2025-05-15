def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

#lst=list(map(int,input("enter the input: ").split()))
lst=[45,5,9,31,45,4,8]
even,odd=count(lst)
print(even)
print(odd)

print("even : {} and odd : {}".format(even,odd))


#fibonacci
def fib(x):
    a=0
    b=1
    if x<=0:
        print("its not done")
    elif x==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,x):
            c=a+b
            if c>100: #if you remove this line and next you can get values till xhow much you mentioned init
                break
            print(c)
            a=b
            b=c

fib(100)


#factorial
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
a=fact(5)
print("factorila is: ",a)




