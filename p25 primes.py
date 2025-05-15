#checking prime number

a=7
for i in range(2,a):
    if a%i==0:
        print("not prime")
        break
else:
        print("its prime")

#for first 10 prime numbers

def is_prime(n):
    if n<2:
        return False
    for j in range(2,int(n**0.5)+1):
        if n%j==0:
            return False
    else:
        return True
prime=[]
no=2
while len(prime)<10:
    if is_prime(no):
        prime.append(no)
    no+=1
print("the top tenprime numbers are: ",prime)

#for last 10 primes in 1 to 100
pr=[]
for k in range(100,2,-1):
    if is_prime(k):
        pr.append(k)
    if len(pr)==10:
        break
print("last 10 prime values: ",pr)