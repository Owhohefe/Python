class divisor_number(object):
    num = 0

    def test_num (self):
        self.num = int (input("Enter a number: "))
        x = 1
        while x <= self.num:
            if self.num % x == 0:
                print(x)
            x = x + 1


DN = divisor_number()
DN.test_num()
