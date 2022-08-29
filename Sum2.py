import sys

class Sum2:

    def CalcSum(self,x,y):
        u = int(x)
        v = int(y)
        
        total = 0
        
        for i in range(u,v):
            if i % 2 == 0:
                total += i

        print (total)

S = Sum2()
S.CalcSum(sys.argv[1],sys.argv[2])
                
        
