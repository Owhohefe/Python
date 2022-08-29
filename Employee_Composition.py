##import Date_Composition

class Employee_Composition:

    firstName = ""
    lastName = ""
    birthDate = ""
    hireDate = ""

    def __init__(self,first,last,dateOfBirth,dateOfHire):
        self.firstName = first
        self.lastName = last
        self.birthDate = dateOfBirth
        self.hireDate = dateOfHire

    def toString(self):
        Str = "{} {} Birthday:{} Hired:{}"
        return Str.format(self.lastName,self.firstName,self.birthDate,self.hireDate)
        
        
##dateOfBirth = Date_Composition()
##dateOfHire = Date_Composition()
