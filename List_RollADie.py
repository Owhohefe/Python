import random

class List_RollADie:

    frequency = [0,0,0,0,0,0,0]

    def RollADie(self):

        for i in range(6000000):
            
            face = random.randint(1,6)

            if face == 1:
                self.frequency[1] += 1
            elif face == 2:
                self.frequency[2] += 1
            elif face == 3:
                self.frequency[3] += 1
            elif face == 4:
                self.frequency[4] += 1
            elif face == 5:
                self.frequency[5] += 1
            elif face == 6:
                self.frequency[6] += 1

    def printList(self):
##        print("Face"+"\t"+"Frequency")
##
##        for Face in range(1,7):
##            print("%d\t%d"%(Face,self.frequency[Face]))

        print("%4s%10s"%("Face","Frequency"))

        for Face in range(1,7):
            print("%4d%10d"%(Face,self.frequency[Face]))
            
        
LR = List_RollADie()
LR.RollADie()
LR.printList()
        
