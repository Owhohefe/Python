class compare_list(object):

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    x =[]
    y =[]

    def compare(self):
        self.x = [num for num in self.a if num in self.b]

    def new_list(self):
        self.y =[num1 for num1 in self.x if num1 not in self.y]

    def print_list(self):           
        print(self.y)


CL = compare_list()
CL.compare()
CL.new_list()
CL.print_list()
