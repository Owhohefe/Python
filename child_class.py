from parent_class import person

class child_class(person):

    def __init__ (self, firstName, lastName, year):
        person.__init__(self, firstName, lastName)
        self.year = year
            
    def print_student(self):
        print("My name is %s,%s and the year is %d" %(self.firstName, self.lastName, self.year))


st = child_class("Efe", "Ekpomebe", 2019.00)
st.printname()
st.print_student()

