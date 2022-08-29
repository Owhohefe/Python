import threading
import time

exitFlag = 0

class print_Name(threading.Thread):

    def __init__(self,threadID, name, counter, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.delay = delay

    def run(self):
        print ("Starting " + self.name)
        print_time(self.name, self.counter, self.delay)
        add_time(self.threadID,self.delay,self.counter)
        print ("Exiting " + self.name)

def print_time(name,delay,counter):
    while counter > 0:
        if exitFlag:
            name.exit()
        time.sleep(delay)
        print(name,time.ctime(time.time()))
        counter -= 1

def add_time(threadID,delay,counter):
    while delay > 0:
        if exitFlag:
            name.exit()
        time.sleep(counter)
        x = threadID * delay
        print(x,time.ctime(time.time()))
        delay -= 1

Thread1 = print_Name(1,"Owhohefe", 1, 5)
Thread2 = print_Name(2,"Ekpomebe", 5, 1)

Thread1.start()
Thread2.start()
Thread1.join()
Thread2.join()
print ("Exiting Main Thread")
