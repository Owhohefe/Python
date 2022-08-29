class BMI:

    def calc_BMI(self, weight, height):
        self.x = weight/height

    def print_BMI(self):
        print("The BMI is %.2f" %(self.x))

BMI = BMI()
BMI.calc_BMI(150,6)
BMI.print_BMI()

    
