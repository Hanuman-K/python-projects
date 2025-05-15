from abc import ABC,abstractmethod
class computer(ABC):
    @abstractmethod
    def process(self):
        pass
class laptop(computer):
    def process(self):
        print("its running")
class whiteboard(computer):
    def write(self):
        print("its working")
class programmer:
    def work(self,com):
        print("solving bugs")
        com.process()
        com.write()

com2=whiteboard()
com1=laptop()
prog1=programmer()
prog1.work(com2)




