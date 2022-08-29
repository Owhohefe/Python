
class InitArray:

    def getEvenNumbers(self):
        self.x = []

        for i in range(2,21):
            if i%2==0:
                self.x.append(i)

    def printList(self):
        print("Index"+"\t"+"Value")

        for i in range(10):
            print("%s\t%s"%(i,self.x[i]))

IA = InitArray()
IA.getEvenNumbers()
IA.printList()


        
