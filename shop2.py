class shop2(object):
    dict = {'Shoe':3, 'Belt':2, 'Bag':4}
    cart = {}
    cost = 0
    x = "yes"

    def buy_goods(self):

        while self.x == "yes":
            choice = input("The goods available are: Shoe, Belt & Bag. Please make your choice: ")
            if choice == 'Shoe':
                quantity = int(input("Please enter quantity: "))
                self.cart['Shoe'] = quantity
                price = self.dict["Shoe"] * quantity 
                self.cost = self.cost + price
                self.x = input("Do you want to buy another product? yes or no: ")
                print()

            elif choice == 'Belt':
                quantity = int(input("Please enter quantity: "))
                self.cart['Belt'] = quantity
                price = self.dict['Belt'] * quantity
                self.cost = self.cost + price
                self.x = input("Do you want to buy another product? yes or no: ")
                print()

            elif choice == 'Bag':
                quantity = int(input("Please enter quantity: "))
                self.cart['Bag'] = quantity
                price = self.dict['Bag'] * quantity
                self.cost = self.cost + price
                self.x = input("Do you want to buy another product? yes or no: ")
                print()


    def display_cart(self):
        view_cart = input("Do you want to view your cart? yes or no: ")
        if view_cart == "yes":
            print("Product","\t", "Quantity")
            for i,j in self.cart.items():
                print(i,"\t\t",j)

    def make_payment(self):
        pay = input("Do you want to make payment now? yes or no: ")
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
            print("continue shopping")
            sh.buy_goods()

sh = shop2()
sh.buy_goods()
sh.display_cart()
sh.make_payment()
