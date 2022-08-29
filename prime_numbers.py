class prime_number (object):

    x = 2

    y = []

    z = []

    smallest = None

    def determine_prime(self):
        num = int(input("Enter a number: "))  
        while self.x < num:
            self.y.append (self.x)
            self.x = self.x + 1

        for a in self.y:
            c = num % a
            self.z.append(c)

        for b in self.z:
            if self.smallest is None or b < self.smallest:
                self.smallest = b

        if self.smallest != 0:
            print (num, "is a prime number")        
        else:
            print (num, "is not a prime number")


pn = prime_number()
pn.determine_prime()
