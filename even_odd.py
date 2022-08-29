class even_odd(object):
    num = 0

    def even_test(self):
        self.num = int(input("Enter a number: "))

        if self.num % 2 ==0:
            print(self.num,"is an even number")
        else:
            print(self.num,"is an odd number")


EV = even_odd()
EV.even_test()
