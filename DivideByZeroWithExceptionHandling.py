
class DivideByZeroWithExceptionHandling:

    def quotient(self, numerator, denominator):
        return numerator/denominator

    def main(self):
        z = True
        while z:
            try:
                x = int(input("Enter the numerator: "))
                y = int(input("Enter the denominator: "))
                result = self.quotient(x,y)
                print("Result: %d/%d = %d"%(x,y,result))
                z = False
            except ZeroDivisionError as e:
                print("Zero is an invalid denominator. Please try again.\n")
            except ValueError as e:
                #print(e)
                print("You must enter integer values. Please try again.\n")
            except Exception as e:
                print("An unexpected error occured. Please try again.\n")
        
DBZ = DivideByZeroWithExceptionHandling()
DBZ.main()
