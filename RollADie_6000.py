import random

class RollADie_6000:

    frequency1 = 0
    frequency2 = 0
    frequency3 = 0
    frequency4 = 0
    frequency5 = 0
    frequency6 = 0

    def rolldie(self):
	
        for i in range(6000):
            face = random.randint(1,6)

            if face == 1:
                RollADie_6000.frequency1 +=1
            elif face == 2:
                RollADie_6000.frequency2 +=1
            elif face == 3:
                RollADie_6000.frequency3 +=1
            elif face == 4:
                RollADie_6000.frequency4 +=1
            elif face == 5:
                RollADie_6000.frequency5 +=1
            elif face == 6:
                RollADie_6000.frequency6 +=1

    def printFrequency(self):
        print("Face\tFrequency")
        print("1\t%d\n2\t%d\n3\t%d\n4\t%d\n5\t%d\n6\t%d\n" %(RollADie_6000.frequency1,
                                                             RollADie_6000.frequency2,
                                                             RollADie_6000.frequency3,
                                                             RollADie_6000.frequency4,
                                                             RollADie_6000.frequency5,
                                                             RollADie_6000.frequency6))

RAD = RollADie_6000()
RAD.rolldie()
RAD.printFrequency()
