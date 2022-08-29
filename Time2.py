
class Time2:

    __hour = 0
    __minute = 0
    __second = 0

##    def __init__(self):
##        self.__init__(0,0,0)
##
##    def __init__(self,h):
##        self.__init__(h,0,0)
##
##    def __init__(self,h,m):
##        self.__init__(h,m,0)

    def __init__(self,h,m,s):
        self.setTime(h,m,s)

##    def __init__(self,time):
##        self.__init__(time.getHour(), time.getMinute(), time.getSecond())

    def setHour(self,h):
        if(h>=0 and h<24):
            self.__hour = h
        else:
            raise ValueError("hour is out of range")

    def setMinute(self,m):
        if(m>=0 and m<60):
            self.__minute = m
        else:
            raise ValueError("minute is out of range")

    def setSecond(self,s):
        if(s>=0 and s<60):
            self.__second = s
        else:
            raise ValueError("second is out of range")

    def getHour(self):
        return self.__hour

    def getMinute(self):
        return self.__minute
    
    def getSecond(self):
        return self.__second

    def setTime(self,h,m,s):
        self.setHour(h)
        self.setMinute(m)
        self.setSecond(s)

    def toUniversalString(self):
        String = "{}:{}:{}"
        return String.format(self.__hour,self.__minute,self.__second)
          
    def toStandardString(self):
        Str = "{}:{}:{} {}"
        return Str.format((12 if (self.__hour==0 or self.__hour==12) else (self.__hour%12)),self.__minute,self.__second,("AM" if self.__hour < 12 else "PM"))


##t1 = Time2()
##t2 = Time2(2)
##t3 = Time2(21,34)
t4 = Time2(12,25,42)
##t5 = Time2(t4)

print(t4.toUniversalString())
print(t4.toStandardString())
