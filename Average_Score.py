class Average_Score:

    courseName = ""

    def __init__(self, name):
        self.courseName = name

    def getCourseName(self):
        return self.courseName

    def displayName(self):
        print("Welcome to the %s course" %(self.getCourseName()))

    def determineClassAverage(self):
        counter = 0
        total = 0
        average = 0
        
        score = int(input("Enter score or -1 to quit: "))
        
        while score != -1:
            total = total + score
            counter = counter + 1
            score = int(input("Enter score or -1 to quit: "))
            
        if counter != 0:
            average = total/counter
            print("The sum of the %d scores is %d" %(counter,total))
            print("The average score is %d" %(average))
        else:
            print("No score was entered")
            


