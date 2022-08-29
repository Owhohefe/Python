import threading
import time

exitFlag = 0

class print_Name(threading.Thread):

    def __init__(self,threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print ("Starting " + self.name)
        print_time(self.name, self.counter, 5)
        print ("Exiting " + self.name)

def print_time(name,delay,counter):
    while counter > 0:
        if exitFlag:
            name.exit()
        time.sleep(delay)
        print(name,time.ctime(time.time()))
        counter -= 1


Thread1 = print_Name(1,"Owhohefe", 2)
Thread2 = print_Name(2,"Ekpomebe", 5)

Thread1.start()
Thread2.start()
Thread1.join()
Thread2.join()
print ("Exiting Main Thread")
    
