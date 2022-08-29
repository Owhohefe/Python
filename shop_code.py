class shop_code:
    products = ["Shoe","Bag","Belt"]
    quantity = [4, 5, 6]
    price = [4, 3, 2]

    choice_product =""
    choice_quantity =0

    cost = 0
    payment = 0

    x = "yes"

    def buy_product(self):      

        while self.x == "yes":
            print ("The products available with their quantity and price are as shown below")
            print ("products","\t", "quantity","\t","price")
            for i in range(len(self.products)):
                print(self.products[i],"\t\t",self.quantity[i],"\t\t",self.price[i])
            print("\n")
            
            self.choice_product = input("Please choose a product: ")
            if self.choice_product == "Shoe":
                self.choice_quantity = int(input("Please enter quantity: "))
                if self.choice_quantity > self.quantity[0]:
                    print("We don't have up to that quantity")
                    print("Please enter quantity less than or equal to",self.quantity[0])
                    self.choice_quantity = int(input())
                self.cost = self.cost +(self.choice_quantity * self.price[0])
                self.quantity[0] = self.quantity[0] - self.choice_quantity
                self.x = input ("Do you want to buy another product. yes or no: ")
                print("\n")
                
            elif self.choice_product == "Bag":
                self.choice_quantity = int(input("Please enter quantity: "))
                if self.choice_quantity > self.quantity[1]:
                    print("We don't have up to that quantity")
                    print("Please enter quantity less than or equal to",self.quantity[1])
                    self.choice_quantity = int(input())
                self.cost = self.cost +(self.choice_quantity * self.price[1])
                self.quantity[1] = self.quantity[1] - self.choice_quantity
                self.x = input ("Do you want to buy another product. yes or no: ")
                print("\n")

            elif self.choice_product == "Belt":
                self.choice_quantity = int(input("Please enter quantity: "))
                if self.choice_quantity > self.quantity[2]:
                    print("We don't have up to that quantity")
                    print("Please enter quantity less than or equal to",self.quantity[2])
                    self.choice_quantity = int(input())
                self.cost = self.cost +(self.choice_quantity * self.price[2])
                self.quantity[2] = self.quantity[2] - self.choice_quantity
                self.x = input ("Do you want to buy another product. yes or no: ")
                print("\n")
            

    def make_payment(self):
        print("The cost of the products is:", self.cost)
        self.payment = int(input("Please make your payment: "))
        if self.payment == self.cost:
            print("Thank you for shopping with us. You may leave with the goods.")
        elif self.payment > self.cost:
            print("Take your change of",(self.payment-self.cost))
            print("Thank you for shopping with us. You may leave with the goods.")
        else:
            print("You have paid less by", (self.cost - self.payment),".Please pay the correct amount")
            shop.make_payment()

shop = shop_code()
shop.buy_product()
shop.make_payment()
