from time import sleep
from threading import*
class hello(Thread):  #we use htread to run it seperately(i.e, seperate thread not in main thread)
    def run(self):
        for i in range(5):
            print("hello",i)
            sleep(1) #wait for 1sec and then print

class hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)
t1=hello()
t2=hi()
t1.start()
sleep(0.2) #this sleep is to avoid collision of hello and hi thread (if after sleep of 1sec they both start at same time)
t2.start()

t1.join() #we are asking the main thread to wait until the whole t1,t2 o/p's are done
t2.join()
print("bye")
