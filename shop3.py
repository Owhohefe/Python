class shop2(object):
    dict = {'Shoe':3, 'Belt':2, 'Bag':4}
    cart = {}
    cost = 0
    x = "yes"
    y = "yes"

    def buy_goods(self):
        print ("The products available are as shown below: ")
        print("Product","\t", "Price")
        for a,c in self.dict.items():
            print (a,"\t\t",c)
        print ()

        while self.x == "yes":
            choice = input("Please enter the name of the product you want to purchase: ")
            quantity = int(input("Please enter the quantity of the product you want: "))
            self.cart[choice] = quantity
            self.x = input("Do you want to buy another product? yes or no: ")
            print()

    def display_cart(self):
        view_cart = input("Do you want to view your cart? yes or no: ")
        if view_cart == "yes":
            print("Product","\t", "Quantity")
            for i,j in self.cart.items():
                print(i,"\t\t",j)
            print()    
        else:
            print()
                
    def modify_cart(self):
        mod_cart = input("Do you want to modify your cart? yes or no: ")
        if mod_cart == "yes":
            '''print("Product","\t", "Quantity","\t", "Cost" )
            for i,j in self.cart.items():
                print(i,"\t\t",j,"\t\t",(j*self.dict(i) )
            print()'''
            
            while self.y == "yes":
                mod_choice = input("Please enter the product you want to modify its quantity: ")
                quantity = int(input("Please enter the new quantity: "))
                self.cart[mod_choice] = quantity
                self.y = input("Do you want to modify the quantity of another product? yes or no: ")
                print()
            sh.display_cart()
                
        else:
            print()

    def compute_cost(self):
        for b in self.cart:
            self.cost = self.cost + (self.cart[b] * self.dict[b])
            
    def make_payment(self):
        pay = input("Do you want to check out now? yes or no: ")
        if pay == "yes":
            print("The cost of the products is:", self.cost)
            self.payment = int(input("Please make your payment: "))
            if self.payment == self.cost:
                print("Thank you for shopping with us. You may leave with the goods.")
            elif self.payment > self.cost:
                print("Take your change of",(self.payment-self.cost))
                print("Thank you for shopping with us. You may leave with the goods.")
            else:
                print("You have paid less by", (self.cost - self.payment),".Please pay the correct amount")
                sh.make_payment()
        else:
            print("Do you want to continue shopping?")
            shop_or_exit = input("Enter yes to continue or no to exit: ")
            if shop_or_exit == "yes":
                sh.buy_goods()
            elif shop_or_exit == "no":
                print ("Thank you for visiting our site")

sh = shop2()
sh.buy_goods()
sh.display_cart()
sh.modify_cart()
sh.compute_cost()
sh.make_payment()
