class shop (object):

    QBag = 20
    QBelt = 10
    QShoe = 30

    PBag = 2
    PBelt = 3
    PShoe = 6

    
    def buy(self):
        choice = input ("\nThe products available for purchase are: \nBag \nBelt \nShoe \n\nPlease pick a product:  ")
        if choice == "Bag":
            print ("Available Quantity = ",self.QBag,"Price = ",self.PBag)
            Quantity = int (input("\nPlease enter the number of bags you want to buy: "))
            if Quantity > self.QBag:
                print("\nwe are out of stock. Please pick another product or reduce the quantity to what we have in stock")
                sh.buy()
            elif Quantity <= self.QBag:
                cost = Quantity*self.PBag
                print ("\nThe cost of the bags will be: ",cost)
                amt = int(input("\nPlease enter the amount you are paying: "))
                if amt < cost:
                    print("\nYou have not paid the correct amount")
                    sh.buy()
                elif amt == cost:
                    print ("\nThank you for shopping with us")
    
        if choice == "Belt":
            print ("Available Quantity = ",self.QBelt,"Price = ",self.PBelt)
            Quantity = int (input("\nPlease enter the number of Belt you want to buy: "))
            if Quantity > self.QBelt:
                print("\nwe are out of stock. Please pick another product or reduce the quantity to what we have in stock")
                sh.buy()
            elif Quantity <= self.QBelt:
                cost = Quantity*self.PBelt
                print ("\nThe cost of the Belt will be: ",cost)
                amt = int(input("\nPlease enter the amount you are paying: "))
                if amt < cost:
                    print("\nYou have not paid the correct amount")
                    sh.buy()
                elif amt == cost:
                    print ("\nThank you for shopping with us")

        if choice == "Shoe":
            print ("Available Quantity = ",self.QShoe,"Price = ",self.PShoe)
            Quantity = int (input("\nPlease enter the number of Shoe you want to buy: "))
            if Quantity > self.QShoe:
                print("\nwe are out of stock. Please pick another product or reduce the quantity to what we have in stock")
                sh.buy()
            elif Quantity <= self.QShoe:
                cost = Quantity*self.PShoe
                print ("\nThe cost of the Shoe will be: ",cost)
                amt = int(input("\nPlease enter the amount you are paying: "))
                if amt < cost:
                    print("\nYou have not paid the correct amount")
                    sh.buy()
                elif amt == cost:
                    print ("\nThank you for shopping with us")


sh = shop()
sh.buy()
        
