
class CommissionEmployee:

    __firstName = ""
    __lastName = ""
    __socialSecurityNumber = ""
    __grossSales = 0.0
    __commissionRate = 0.0

    def __init__(self,first,last,ssn,sales,rate):
        self.__firstName = first
        self.__lastName = last
        self.__socialSecurityNumber = ssn
        self.setGrossSales(sales)
        self.setCommissionRate(rate)

    def setFirstName(self,first):
        self.__firstName = first

    def getFirstName(self):
        return self.__firstName

    def setLastName(self,last):
        self.__lastName = last

    def getLastName(self):
        return self.__lastName

    def setSocialSecurityNumber(self,ssn):
        self.__socialSecurityNumber = ssn

    def getSocialSecurityNumber(self):
        return self.__socialSecurityNumber

    def setGrossSales(self,sales):
        if sales >= 0.0:
            self.__grossSales = sales
        else:
            raise ValueError("Gross sales must be >= 0.0")
        
    def getGrossSales(self):
        return self.__grossSales

    def setCommissionRate(self,rate):
        if rate > 0.0 and rate < 1.0:
            self.__commissionRate = rate
        else:
            raise ValueError("Commission rate must be > 0.0 and < 1.0")

    def getCommissionRate(self):
        return self.__commissionRate

    def earnings(self):
        return self.__commissionRate * self.__grossSales
            
    def toString(self):
        Str = "commission employee:{} {}\nsocial security number: {}\ngross sales: {}\ncommission rate: {}"
        return Str.format(self.__firstName,self.__lastName,self.__socialSecurityNumber,self.__grossSales,self.__commissionRate)
        










    





    
