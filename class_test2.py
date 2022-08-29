import datetime as dt

class Members:

    expiry_days = 90       

    def __init__(self, fname, sname):
        self.first_name = fname
        self.second_name = sname
        self.expiry_date = dt.date.today()+ dt.timedelta(days=self.expiry_days)

    def show_expiry(self):
        return f"{self.first_name} {self.second_name} expires on {self.expiry_date:%d/%m/%y}"
        



class Admin(Members):
    expiry_days = 365 * 100

    def __init__(self, fname, sname, secretcode):
        super().__init__(fname, sname)
        self.secretcode = secretcode
    


class Users(Members):
    pass


Dulen = Admin("Dulen", "Kpenetese","secret")

print(Dulen.first_name)
print(Dulen.second_name)
print(Dulen.expiry_date)
print(Dulen.secretcode)
print(Dulen.show_expiry())

Efe = Users("Owhohefe", "Ekpomebe")

print(Efe.first_name)
print(Efe.second_name)
print(Efe.expiry_date)

        
