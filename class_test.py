import datetime as dt

class Members:
    first_name = ""
    second_name = ""

    #def __init__(self, fname, sname):
        #self.first_name = fname
        #self.second_name = sname
        #self.date_joined = dt.date.today()
        #self.is_active = True

    def create_members(self,fname, sname):
        self.first_name = fname
        self.second_name = sname
        self.date_joined = dt.date.today()
        self.is_active = True

    def say_hello(self):
        print("Hello "+self.first_name+" "+self.second_name+"."+" You joined on %s" %(self.date_joined))


#Efe = Members("Owhohefe", "Ekpomebe")
#Ben = Members("Ben", "Okoli")

M1 = Members()
M2 = Members()

M1.create_members("Owhohefe","Ekpomebe")
M2.create_members("Ben","Okoli")

#Efe.say_hello()
#Ben.say_hello()

M1.say_hello()
M2.say_hello()

#print(Efe.first_name)
#print(Ben.second_name)

print(M1.first_name)
print(M2.second_name)

#Members.say_hello(M1)
        
