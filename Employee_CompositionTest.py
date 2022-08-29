##import Date_Composition
from Date_Composition import *
##import Employee_Composition
from Employee_Composition import *

class Employee_CompositionTest:


    def Compose(self):
        pass

DoB = Date_Composition(7,24,1949)
DoH = Date_Composition(3,12,1988)
employee = Employee_Composition("Bob","Blue",DoB.getDate(),DoH.getDate())
print(employee.toString())
