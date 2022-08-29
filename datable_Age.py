class datable_Age:

    def datable_age(self,my_age):
        girls_age = my_age/2 + 7
        return girls_age

    def printAge(self):
        print("Age"+"\t"+"Age Limit")
        for x in range(18,40):
            limit=self.datable_age(x)
            print(x,"\t",limit)


d_Age = datable_Age()
d_Age.printAge()
