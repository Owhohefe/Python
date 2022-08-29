import random

class game (object):

    x = 1
    y = []
    num = ""
    a = random.randint(1, 9)

    str1 = "play"

    def play_game (self):
        while self.num != self.a or self.num != "exit":
            num = input("Enter a number: ")
            if num == "exit":
                break
            num = int(num)
            if num < self.a:
                print ("You guessed too low!")
            elif num > self.a:
                print ("You guessed too High!")
            else:
                print ("You guessed correctly!")

            self.y.append (num)            

    def print_num(self):
        print ("\n\nThe number of try's and your guesses are")
        print ("TRY\t","Number")
        for num1 in self.y:
            print (self.x,"\t", num1)
            self.x = self.x + 1

GA = game ()
GA.play_game()
GA.print_num()
