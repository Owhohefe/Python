import random

class StudentPoll:

    responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]
    
    frequency = [0,0,0,0,0,0]

    def detFrequency(self):

        for i in range(20):
            
            face = self.responses[i]
            
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

    def printResponses(self):
##        print("Face"+"\t"+"Frequency")
##
##        for Face in range(1,7):
##            print("%d\t%d"%(Face,self.frequency[Face]))

        print("%8s%10s"%("Response","Frequency"))

        for Face in range(1,6):
            print("%8d%10d"%(Face,self.frequency[Face]))
            
        
SP = StudentPoll()
SP.detFrequency()
SP.printResponses()
        
