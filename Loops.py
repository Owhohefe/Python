class Loops:
    x = 10
    count = 0
    course = "python programming"

    def WhileLoop(self):
        print ("While loops")
        while self.count < self.x:
            self.count +=1
            if self.count == 5:
                continue
            print ("count is: ", self.count)

    def ForLoop(self):
        print("For Loops")
        for i in range(5):
            if i == 3:
                continue
            print(i)

    def getAlpha(self):
        for c in self.course:
            if c == "h":
                continue
            print(c)

L = Loops()
L.WhileLoop()
L.ForLoop()
L.getAlpha()
