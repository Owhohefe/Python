import random

class Craps:

    def rollDie(self):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        Sum = die1 + die2

        print("You rolled %d + %d = %d"%(die1,die2,Sum))

        return Sum

    def CheckRolls(self):
        SumOfDice = self.rollDie()

        if SumOfDice == 7 or SumOfDice == 11:
            print("You rolled %d on first throw. You win!!"%(SumOfDice))
            
        elif SumOfDice == 2 or SumOfDice == 3 or SumOfDice == 12:
            print("You rolled %d on first throw. You lose!!" %(SumOfDice))

        elif SumOfDice == 4 or SumOfDice == 5 or SumOfDice == 6 or SumOfDice == 8 or SumOfDice == 9 or SumOfDice == 10:
            point = SumOfDice
            SumofDice1 = 0
            print("You rolled %d on first throw. point is %d.\n" %(SumOfDice,point))

            while SumofDice1 != point:
                
                SumofDice1 = self.rollDie()
                
                if SumofDice1 == 7:
                    print("You rolled 7 after rolling %d as point. You lose!!" %(point))
                    break
                
                elif SumofDice1 == point:
                    print("You rolled %d after rolling %d as point. You win!!" %(SumofDice1,point))

                else:
                    print("Continue")
                    

C = Craps()
C.CheckRolls()
