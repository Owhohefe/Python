import time

class print_Name:
    count = 0

    def Name(self):
        while self.count < 5:
            time.sleep(2)
            self.count += 1
            print("Owhohefe",time.ctime(time.time()))


PN = print_Name()
PN.Name()
