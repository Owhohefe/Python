class Grade_Analysis:

    def passFail(self):
        x = 0
        count_pass = 0
        count_fail = 0

        while x < 10:
            grade = int(input("Enter result (1 = pass, 2 = fail): "))
            if grade == 1:
               count_pass = count_pass + 1
            elif grade == 2:
                count_fail = count_fail + 1

            x = x + 1

        print("%d students passed the exam" %(count_pass))
        print("%d students failed the exam" %(count_fail))

        if count_pass > 8:
            print("Bonus to instructor!")

GA = Grade_Analysis()
GA.passFail()
