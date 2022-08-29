class MaximumFinder:

    def maximum(self,x,y,z):
        maximumValue = x

        if y > maximumValue:
            maximumValue = y

        if z > maximumValue:
            maximumValue = z

        return maximumValue

    def display_Max(self):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))

        result = self.maximum(num1,num2,num3)

        print("The maximum number is %.2f"%(result))

MF = MaximumFinder()
MF.display_Max()
        
        
