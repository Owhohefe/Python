import time

class print_Surname:
    count = 0

    def SurName(self):
        while self.count < 5:
            time.sleep(2)
            self.count += 1
            print("Owhohefe",time.ctime(time.time()))


PN = print_Surname()
PN.SurName()
