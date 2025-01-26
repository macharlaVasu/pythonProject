from threading import *
from time import sleep

class Hellow(Thread):
    def run(self):
        for i in range(5):
            print("Hellow")
            sleep(1)



class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

obj1 = Hellow()
obj2 = Hi()
obj1.start()
obj2.start()

obj1.join()
obj2.join()
print("Bye")
