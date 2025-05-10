        
from threading import Thread
from time import sleep

class hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello, world!")
            sleep(1)

        
class goodbye(Thread):
    def run(self):
        for i in range(5):
            print("Hello, world!")
            sleep(1)



OBJ = hello()
OBJ2 = goodbye()

OBJ.start()
OBJ2.start()    

