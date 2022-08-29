from CommissionEmployee import *
from BasePlusCommissionEmployee import *

class PolymorphismTest:

    pass


CE = CommissionEmployee("Sue","Jones","222-22-2222",10000,.06)
BCE = BasePlusCommissionEmployee("Bob","Lewis","333-33-3333",5000,.04,300)

print(CE.toString())
print()
print(BCE.toString())

    
