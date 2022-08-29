


class ListManipulations:

    def manipulateList(self):
        floatList = [8.4,9.3,0.2,7.9,3.4]
        floatList.sort()

        print("floatList: ",end="")
        for i in floatList:
            print(i,end=" ")
        print()

        intList = [1,2,3,4,5,6]
        #intListCopy = []
        intListCopy = intList.copy()
        self.displayList(intList,"intList")
        self.displayList(intListCopy,"intListCopy")

        location = intList.index(5)
        if location >=0:
            print("Found 5 at element %d in intList\n"%(location))
        else:
            print("5 not found in intArray")

        location = intList.index(8763)
        if location >=0:
            print("Found 8763 at element %d in intList\n"%(location))
        else:
            print("8763 not found in intArray")
  

    def displayList(self,L,description):
        print("%s: "%(description),end="")

        for i in L:
            print(i,end=" ")
        print()

LM = ListManipulations()
LM.manipulateList()
        
            

        
        
