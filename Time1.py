
class Time1:

    __hour = 0
    __minute = 0
    __second = 0

    def setTime(self,h,m,s):
        if((h>=0 and h<24)and(m>=0 and m<60)and(s>=0 and s<60)):
            self.__hour = h
            self.__minute = m
            self.__second = s
        else:
            raise ValueError("hour, minute and/or second was out of range")

    def toUniversalString(self):
        String = "{}:{}:{}"
        return String.format(self.__hour,self.__minute,self.__second)
          
    def toStandardString(self):
        Str = "{}:{}:{} {}"
        return Str.format((12 if (self.__hour==0 or self.__hour==12) else (self.__hour%12)),self.__minute,self.__second,("AM" if self.__hour < 12 else "PM"))


T1 = Time1()
T1.setTime(13,54,23)
print(T1.toUniversalString())
print(T1.toStandardString())
    
T2 = Time1()
try:
    T2.setTime(93,54,23)
except ValueError as e:
    print(e)
    
print(T2.toUniversalString())
print(T2.toStandardString())
