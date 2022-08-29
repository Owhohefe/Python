class GradeBook3:

    __courseName=""
    __grades=[]

    def __init__(self,name,gradeList):
        
        self.__courseName = name
        self.__grades = gradeList

    def setCourseName(self,name):
        self.__courseName = name

    def getCourseName(self):
        return self.__courseName

    def displayMessage(self):
        print("Welcome to the grade book for %s!\n\n"%(self.getCourseName()))

    def processGrades(self):
        self.outputGrades()

        print("\nClass average is %.2f\n"%(self.getAverage()))

        print("Lowest grade is %d\nHighest grade is %d\n\n"%(self.getMinimum(), self.getMaximum()))

        self.outputBarChart()

    def getMinimum(self):
        lowestGrade = self.__grades[0]
        for grade in self.__grades:
            if grade < lowestGrade:
                lowestGrade = grade
        return lowestGrade

    def getMaximum(self):
        highestGrade = self.__grades[0]
        for grade in self.__grades:
            if grade > highestGrade:
                highestGrade = grade
        return highestGrade

    def getAverage(self):
        total = 0.0

        for grade in self.__grades:
            total = total + grade

        return total/len(self.__grades)

    def outputBarChart(self):
        print("Grade Distribution: ")

        frequency = [0,0,0,0,0,0,0,0,0,0,0]

        for grade in self.__grades:
            if grade > 0 and grade < 10:
                frequency[0]=frequency[0] + 1
            elif grade > 10 and grade < 20:
                frequency[1]=frequency[1] + 1
            elif grade > 20 and grade < 30:
                frequency[2]=frequency[2] + 1
            elif grade > 30 and grade < 40:
                frequency[3]=frequency[3] + 1
            elif grade > 40 and grade < 50:
                frequency[4]=frequency[4] + 1
            elif grade > 50 and grade < 60:
                frequency[5]=frequency[5] + 1
            elif grade > 60 and grade < 70:
                frequency[6]=frequency[6] + 1
            elif grade > 70 and grade < 80:
                frequency[7]=frequency[7] + 1
            elif grade > 80 and grade < 90:
                frequency[8]=frequency[8] + 1
            elif grade > 90 and grade < 100:
                frequency[9]=frequency[9] + 1
            elif grade == 100:
                frequency[10]=frequency[10] + 1
        
        for i in range(len(frequency)):
            if i == 10:
                print("%5d: "%(100),end="")
            else:
                print("%02d-%02d: "%(i*10,i*10+9),end="")

            for stars in range (frequency[i]):
                print("*",end="")

            print()


    def outputGrades(self):
        print("The Grades are: \n")

        for i in range (len(self.__grades)):
            print("Student %2d: %3d\n"%(i+1,self.__grades[i]))



        
                
            
        
        

        

    
