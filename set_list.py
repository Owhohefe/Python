class set_list(object):

    y = []

    z = []

    nums = set()

    def get_list(self):
        num = int(input("How many numbers do you want in the list? "))
        x = 0
        while x < num:
            num1 = int (input("Enter the numbers? "))
            self.y.append(num1)
            x += 1

    def get_set(self):
        for num2 in self.y:
            self.nums.add(num2)

    def print_set(self):
        for num3 in self.nums:
            self.z.append(num3)
        print(self.z)

sl = set_list()
sl.get_list()
sl.get_set()
sl.print_set()
    

