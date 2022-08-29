class Amount:

    def CalcAmount(self):
        
        Amount = 0
        Principal = 1000
        Rate = 0.05
        print("Year\tAmount")
        for i in range(1,11):
            Amount = Principal*((1+Rate)**i)
            print("%d\t%.2f" %(i,Amount))
            

A = Amount()
A.CalcAmount()
                
        
