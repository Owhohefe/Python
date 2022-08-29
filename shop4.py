class shop4(object):
    dict = {'SHOE':3, 'BELT':2, 'BAG':4, 'TOWEL':4}
    cart = {}
    cost = 0
    x = "YES"
    y = "YES"

    def buy_goods(self):
        print ("The products available are as shown below: ")
        print("PRODUCT","\t", "PRICE(=N=)")
        print("---------------------------")
        for a,c in self.dict.items():
            print (a,"\t\t",c)
        print ()
        while self.x == "YES":
            choice = input("Please enter the name of the product you want to purchase: ").upper()
            if choice in self.dict:
                p = 0
                while p == 0:
                    try:
                        quantity = abs(int(input("Please enter the quantity of the product you want: ")))
                        p = 1
                    except:
                        print("You have to enter the quantity as a whole number")
                        
                self.cart[choice] = quantity
                self.x = input("Do you want to buy another product? yes or no: ").upper()
                print()
            else:
                print("The product chosen is not in stock.")
                self.x = input("Do you want to buy another product? yes or no: ").upper()
                
    def display_cart(self):
        self.cost = 0
        sh.compute_cost()
        view_cart = input("Do you want to view your cart? yes or no: ").upper()
        if view_cart == "YES":
            print("PRODUCT","\t", "QUANTITY","\t", "COST(=N=)")
            print("------------------------------------------")
            for i in self.cart:
                print(i,"\t\t",self.cart[i],"\t\t",(self.cart[i]*self.dict[i]))
            print("------------------------------------------")
            print("TOTAL COST","\t\t\t", self.cost)
            print()    
        else:
            print()
                
    def modify_cart(self):
        mod_cart = input("Do you want to modify your cart? yes or no: ").upper()
        print()
        if mod_cart == "YES":            
            while self.y == "YES":
                mod_choice = input("Please enter the product you want to modify its quantity: ").upper()
                if mod_choice in self.cart:
                    q = 0
                    while q == 0:
                        try:
                            quantity = abs(int(input("Please enter the new quantity: ")))
                            q = 1
                        except:
                            print("You have to enter the quantity as a whole number")
                    if quantity == 0:
                        self.cart.pop(mod_choice)
                    else:    
                        self.cart[mod_choice] = quantity
                    self.y = input("Do you want to modify the quantity of another product? yes or no: ").upper()
                    print()
                else:
                    print("The product chosen is not in the cart.")
                    self.y = input("Do you want to modify the quantity of another product? yes or no: ").upper()
                    print()
            sh.display_cart()      
        else:
            print()

    def compute_cost(self):
        for b in self.cart:
            self.cost = self.cost + (self.cart[b] * self.dict[b])
            
    def make_payment(self):
        pay = input("Do you want to check out now? yes or no: ").upper()
        if pay == "YES":
            print("The cost of the products is: =N=",self.cost)
            self.payment = int(input("Please make your payment: "))
            if self.payment == self.cost:
                print("Thank you for shopping with us. You may leave with the goods.")
            elif self.payment > self.cost:
                print("Please, take your change of =N=",(self.payment-self.cost))
                print("Thank you for shopping with us. You may now leave with the goods.")
            else:
                print("You have paid less by =N=", (self.cost - self.payment),".Please pay the correct amount.")
                sh.make_payment()
        else:
            print("Do you want to continue shopping?")
            shop_or_exit = input("Enter yes to continue or no to exit: ").upper()
            if shop_or_exit == "YES":
                self.x = "YES"
                self.y = "YES"
                sh.buy_goods()
                sh.display_cart()
                sh.modify_cart()
                sh.make_payment()
            elif shop_or_exit == "NO":
                print ("Thank you for visiting our site")

sh = shop4()
sh.buy_goods()
sh.display_cart()
sh.modify_cart()
sh.make_payment()
