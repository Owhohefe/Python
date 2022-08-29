from BasePlusCommissionEmployee import *

class BasePlusCommissionEmployeeTest:

    pass

employee = BasePlusCommissionEmployee("Efe","Ekpomebe","333-33-3333",5000,0.4,300)

print("Employee information obtained by get methods: \n")

print("%s %s"%("First name is",employee.getFirstName()))
print("%s %s"%("Last name is",employee.getLastName()))
print("%s %s"%("Social security number is",employee.getSocialSecurityNumber()))
print("%s %.2f"%("Gross sales is",employee.getGrossSales()))
print("%s %.2f"%("Commission rate is",employee.getCommissionRate()))
print("%s %.2f"%("Base salary is",employee.getBaseSalary()))
print("%s %.2f"%("Earning is",employee.earnings()))

employee.setGrossSales(500)
employee.setCommissionRate(0.1)
print("\n")
print("Updated employee information obtained by toString")
print(employee.toString())
    









    





    
