class List_Sum:

    x = [87,68,94,100,83,78,85,91,76,87]
    y = 0

    def add_ListElements(self):
        for i in self.x:
            self.y = self.y + i

        print(self.y)


LS = List_Sum()
LS.add_ListElements()
        
