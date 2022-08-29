class Area():

    Length = 0

    Breadth = 0

    area = 0

    def CalcArea(self):
        self.Length = float(input("Enter the Length: "))
        self.Breadth = float(input("Enter the Breadth: "))

        self.area = self.Length * self.Breadth       


    def printArea(self):
        
         print("The area of the square or rectangle is %s"%(self.area))


Area1 = Area()

Area1.CalcArea()
        
Area1.printArea()       
