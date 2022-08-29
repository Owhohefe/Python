import sys

class InitArray2:

    def printArray(self, y):

        if len(y)!= 4:
            print("Error: Please re-enter the entire command, including\n"+"an array size, initial value and increment.")
        else:
            listLength = int(y[1])
            List = []

            initialValue = int(y[2])
            increment = int(y[3])

            for i in range (listLength):
                x = initialValue + increment*i
                List.append(x)

            print("%5s%8s"%("Index","Value"))

            for i in range(len(List)):
                print("%5d%8d"%(i,List[i]))

IA2 = InitArray2()
IA2.printArray(sys.argv)
            

        
        
