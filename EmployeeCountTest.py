import EmployeeCount
from EmployeeCount import *

class EmployeeCountTest:
    pass

print("Employees before instantiation: %d\n"%(EmployeeCount.getCount()));

e1 = EmployeeCount("Susan", "Baker")
e2 = EmployeeCount("Bob", "Blue")
e3 = EmployeeCount("Tom", "Jerry")

print("\nEmployees after instantiation: ");
print("via e1.getCount(): %d\n"%(e1.getCount()));
print("via e2.getCount(): %d\n"%(e2.getCount()));
print("via e3.getCount(): %d\n"%(e3.getCount()));
print("via Employee.getCount(): %d\n"%(EmployeeCount.getCount()));

print("\nEmployee 1: %s %s\nEmployee 2: %s %s\nEmployee 3: %s %s\n"%(e1.getFirstName(),e1.getLastName(),
                                                                     e2.getFirstName(),e2.getLastName(),
                                                                     e3.getFirstName(),e3.getLastName()));

