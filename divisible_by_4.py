class divisible_by_4:

    def modulo_4(self):
        for x in range(101):
            if x%4 == 0:
                print (x, "is divisble by 4")


d4 = divisible_by_4()
d4.modulo_4()
