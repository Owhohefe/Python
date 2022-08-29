class person:
    firstName = ""
    lastName = ""

    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        

    def printFullname (self):
        print(self.firstName,self.lastName)

personName = person("Efe","Ekpomebe")
     
personName.printFullname()        
