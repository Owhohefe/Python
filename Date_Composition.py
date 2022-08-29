
class Date_Composition:

    month = 0
    day = 0
    year = 0

    daysPerMonth = [0,31,28,31,30,31,30,31,31,30,31,30,31]

    def __init__(self,theMonth,theDay,theYear):
        self.month = self.checkMonth(theMonth)
        self.year = theYear
        self.day = self.checkDay(theDay)

        print("Date object constructor for date %d/%d/%d\n"%(theMonth,theDay,theYear))
        
    def getDate(self):
        string = "{}/{}/{}"
        return string.format(self.month,self.day,self.year)
        
    def checkMonth(self,testMonth):
        if testMonth>0 and testMonth<=12:
            return testMonth
        else:
            raise ValueError("month must be 1-12")

    def checkDay(self,testDay):
        if testDay>0 and testDay<=self.daysPerMonth[self.month]:
            return testDay
        
        if (self.month == 2 and testDay == 29 and (self.year % 400 == 0 or(self.year % 4 == 0 and self.year % 100 != 0))):
            return testday
        
        raise ValueError("day out-of-range for the specified month and year")

    
