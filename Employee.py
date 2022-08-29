class Employee(object):
    Name = ""
    Age = 0
    Salary = 0
    Desig = ""

    def AcceptEmployee (self):
        print ("Enter Name: ")
        self.Name = input ()
        print ("Enter Age: ")
        self.Age = int (input())
        print ("Enter Salary: ")
        self.Salary = int (input())
        print ("Enter Designation: ")
        self.Desig = input()
        return;

    def DisplayEmployee(self):
        print("Employee Name: ", self.Name)
        print("Employee Age: ", self.Age)
        print("Employee Salary: ", self.Salary)
        print("Employee designation: ", self.Desig)
        return;

Emp = Employee()
Emp.AcceptEmployee()
Emp.DisplayEmployee()

        
    
    
