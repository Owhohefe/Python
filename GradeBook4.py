class GradeBook4:

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

        print("\nLowest grade is %d\nHighest grade is %d\n\n"%(self.getMinimum(), self.getMaximum()))

        self.outputBarChart()

    def getMinimum(self):
        lowestGrade = self.__grades[0][0]
        
        for i in range(len(self.__grades)): 
            for j in range(len(self.__grades[i])):
                if self.__grades[i][j] < lowestGrade:
                    lowestGrade = self.__grades[i][j]
        return lowestGrade

    def getMaximum(self):
        highestGrade = self.__grades[0][0]
        
        for i in range (len(self.__grades)):
            for j in range(len(self.__grades[i])):
                if self.__grades[i][j] > highestGrade:
                    highestGrade = self.__grades[i][j]
        return highestGrade

    def getAverage(self,GList):
        total = 0.0

        for grade in GList:
            total = total + grade

        return total/len(GList)

    def outputBarChart(self):
        print("Grade Distribution: ")

        frequency = [0,0,0,0,0,0,0,0,0,0,0]

        for i in range(len(self.__grades)):
            for j in range(len(self.__grades[i])):

                if self.__grades[i][j] >= 0 and self.__grades[i][j] < 10:
                    frequency[0]=frequency[0] + 1
                elif self.__grades[i][j] >= 10 and self.__grades[i][j] < 20:
                    frequency[1]=frequency[1] + 1
                elif self.__grades[i][j] >= 20 and self.__grades[i][j] < 30:
                    frequency[2]=frequency[2] + 1
                elif self.__grades[i][j] >= 30 and self.__grades[i][j] < 40:
                    frequency[3]=frequency[3] + 1
                elif self.__grades[i][j] >= 40 and self.__grades[i][j] < 50:
                    frequency[4]=frequency[4] + 1
                elif self.__grades[i][j] >= 50 and self.__grades[i][j] < 60:
                    frequency[5]=frequency[5] + 1
                elif self.__grades[i][j] >= 60 and self.__grades[i][j] < 70:
                    frequency[6]=frequency[6] + 1
                elif self.__grades[i][j] >= 70 and self.__grades[i][j] < 80:
                    frequency[7]=frequency[7] + 1
                elif self.__grades[i][j] >= 80 and self.__grades[i][j] < 90:
                    frequency[8]=frequency[8] + 1
                elif self.__grades[i][j] >= 90 and self.__grades[i][j] < 100:
                    frequency[9]=frequency[9] + 1
                elif self.__grades[i][j] == 100:
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
        print("%12s%8s%8s%8s%8s"%("","Test 1","Test 2","Test 3","Average"))
        
        for i in range (len(self.__grades)):
            print("Student %2d: "%(i+1),end="");
            for j in range (len(self.__grades[i])):
                print("%8d"%(self.__grades[i][j]),end="")
                
            print("%8.2f"%(self.getAverage(self.__grades[i])))
            

##GB = GradeBook4()
##GB.outputBarChart()
                
            
        
        

        

    
