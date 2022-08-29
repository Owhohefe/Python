class List_2dimension:

    @staticmethod
    def outputList(List):
        for i in range(len(List)):
            for j in range(len(List[i])):
                print(List[i][j],end=" ")
            print()

array1 = [[1,2,3],[4,5,6]]
array2 = [[1,2],[3],[4,5,6]]

print("Values in array1 by row are")
List_2dimension.outputList(array1)
print("\n")
print("Values in array2 by row are")
List_2dimension.outputList(array2)


##    def main(self):
##        array1 = [[1,2,3],[4,5,6]]
##        array2 = [[1,2],[3],[4,5,6]]
##
##        print("Values in array1 by row are")
##        List_2dimension.outputList(array1)
##        print("\n")
##        print("Values in array2 by row are")
##        List_2dimension.outputList(array2)
##
##L2D = List_2dimension()
##L2D.main()
