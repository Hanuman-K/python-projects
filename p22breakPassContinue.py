a=5
x=int(input("how many candies you want: "))
i=1
while i<=x:
    if i>a:
        print("out of stock")
        break
    else:
        print("candy ",i)
    i+=1

for i in range(1,51):
    if i%2==0 or i%5==0:
        continue  #it skips and goes to next iteration
    print(i)

for i in range (1,11):
    if i%2 != 0:
        pass #Doesn’t affect loop flow or execution.do nothing
    else:
        print(i)



