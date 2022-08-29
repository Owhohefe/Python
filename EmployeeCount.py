class EmployeeCount:

    __firstName = ""
    __lastName = ""
    __count = 0

    def __init__(self,first,last):
        self.__firstName = first
        self.__lastName = last
        EmployeeCount.__count += 1

        print("Employee constructor: %s %s; count = %d\n"%(self.__firstName,self.__lastName,EmployeeCount.__count))


    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName
    
    @staticmethod
    def getCount():
        return EmployeeCount.__count

    
