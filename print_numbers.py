class print_numbers(object):

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    b = []

    lim = 0

    def check_num (self):

        self.lim = int (input("pick a number: "))

        for num in self.a:
            if num < self.lim:
                self.b.append(num)

        print(self.b)

PN = print_numbers()
PN.check_num()
