class check:
    _var1=10

    def __init__(self, sayHello):
        print (sayHello)
    
    def getvariable(self):
        getnum=50
        print (getnum)
        print (self._var1)

    def checkvar (self):
        print (self._var1)
        #print (getnum)

c = check("Welcome to Python")
c.getvariable()
c.checkvar()
        
