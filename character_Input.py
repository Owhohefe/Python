import datetime

class Project_Age(object):
    age = 0
    birth_year = 0
    Year_100 = 0 
    x = datetime.datetime.now()

    def calc_birthyear(self):
        self.age = int(input("Please enter your age: "))
        self.birth_year = self.x.year - self.age
        return;

    def calc_100th_year(self):
        self.Year_100 = self.birth_year + 40
        return;

    def print_year_100(self):
        print("You will be 100 years in",self.Year_100)
        return;
        
PA = Project_Age ()
PA.calc_birthyear()
PA.calc_100th_year()
PA.print_year_100()
        
        

