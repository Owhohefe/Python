#import CommissionEmployee
from CommissionEmployee import *

class BasePlusCommissionEmployee(CommissionEmployee):

    __baseSalary = 0.0

    def __init__(self,first,last,ssn,sales,rate,salary):
        super().__init__(first,last,ssn,sales,rate)
       
        self.setBaseSalary(salary)

    def setBaseSalary(self,salary):
        if salary >= 0.0:
            self.__baseSalary = salary
        else:
            raise ValueError("Base salary must be >= 0.0")
        
    def getBaseSalary(self):
        return self.__baseSalary

    def earnings(self):
        return (self.__baseSalary + (self.getCommissionRate() * self.getGrossSales()))
            
    def toString(self):
        Str = "commission employee:{} {}\nsocial security number: {}\ngross sales: {}\ncommission rate: {}\nbase salary: {}"
        return Str.format(self.getFirstName(),self.getLastName(),self.getSocialSecurityNumber(),self.getGrossSales(),self.getCommissionRate(),self.__baseSalary)
    
        










    





    
