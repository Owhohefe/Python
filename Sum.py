class Sum:

    def CalcSum(self):
        
        total = 0
        
        for i in range(2,21):
            if i % 2 == 0:
                total += i

        print (total)

S = Sum()
S.CalcSum()
                
        
