import random

class RandomIntegers:

    def GenRandInt(self):

        for i in range(1,21):
            
            face = random.randint(1,6)
        
            print (face,end=" ")

            if i % 5 == 0:
                print("\n")

RI = RandomIntegers()
RI.GenRandInt()
        
