amount=int(input("Enter amount: "))
discount = 0

if amount<1000:
    discount=amount*0.05
    print ("Discount",discount)
    
else:
    discount=amount*0.10
    print ("Discount",discount)
    
print ("Net payable:",amount-discount)
