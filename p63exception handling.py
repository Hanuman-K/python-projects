
a=5
b=0
c=a+b   #a/b will not give the output
print(c)

try:
    print(a/b)
except Exception:
    print("hey, you can not divide a number by zero")
print("bye1")

try:
    print(a/b)
except Exception as e:
    print("hey,you cannot divide a no by zero",e) #e will give the error in output why can we do that
print("bye2")

a1=5
b1=2
try:
    print("response open")
    print(a1/b1)
    k=int(input("enter a number"))
    print(k)
except ZeroDivisionError as e: #this helps in execution if b1 = 0
    print("hey,you cannot divide a no by zero",e)
except ValueError as e: #Runs if input is not an integer (like abc or 3.14).
    print("inavlid input")
except Exception as e: #Catches any other unexpected errors (a safety net)
    print("something went wrong")
finally: # Always runs — whether there was an error or not.it should be under try only
    print("resource closed")

