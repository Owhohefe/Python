from time import sleep
from threading import Thread

class hello(Thread):

    def run(self):
        for i in range(5):
            print("hello")

class hi(Thread):

    def run(self):
        for i in range(5):
            print("hi")


t1 = hello()
t2 = hi()

t1.start()
t2.start()

t1.join()
t2.join()

print("Bye")
