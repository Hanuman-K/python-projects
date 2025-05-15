f=open('p6.py','r')
print(f.readline())#it reads only first line
print(f.readline(),end="") #next line without spacing
print(f.readline())
print(f.readline(3)) #only first 3 words in that line
print(f.read())  #if u write this in top it reads all,if its down left over will be read


#write
f1=open('abc.py','w')
f1.write("something\n") #to write anything next line use \n
f1.write("nothing")

#if you clear and write something newly it will get clear in file too but append we have to use
f1=open ("abc.py","a")
f1.write("mobile\n")

#to copy data from my data file to abc file
f=open("p6.py","r")
f1=open("abc.py","w")
for data in f:
    f1.write(data)

#to read binary
h=open("image.png","rb")
h1=open("pasteingimage.png","wb")
for i in h:
    h1.write(i)




