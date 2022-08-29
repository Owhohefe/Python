class GradeBook2:

    __CourseName = ""
    __total = 0
    __gradeCounter = 0
    __aCount = 0
    __bCount = 0
    __cCount = 0
    __dCount = 0
    __fCount = 0

    def __init__(self,name):
        self.__CourseName = name

    def setCourseName(self,name):
        self.__CourseName = name

    def getCourseName(self):
        return self.__CourseName

    def displayMessage(self):
        print("Welcome to the Grade Book for %s"%(self.getCourseName()))

    def inputGrades(self):
        grade = int(input("Enter grade or -1 to stop: "))

        while grade != -1:
            self.__incrementLetterGradeCounter(grade)
            self.__total += grade
            self.__gradeCounter += 1
            grade = int(input("Enter grade or -1 to stop: "))
            

    def __incrementLetterGradeCounter(self, grade):
        if grade >= 90 and grade <= 100:
            self.__aCount += 1
        elif grade >= 80 and grade <= 89:
            self.__bCount += 1
        elif grade >= 70 and grade <= 79:
            self.__cCount += 1
        elif grade >= 60 and grade <= 69:
            self.__dCount += 1
        else:
            self.__fCount += 1
        
    def displayGradeReport(self):
        print("Grade Report: ")

        if self.__gradeCounter != 0:
            Average = self.__total/self.__gradeCounter

            print("Total of the %d grades entered is %d"%(self.__gradeCounter, self.__total))
            print("Class Average is %.2f"%(Average))
            print("\n%s\n%s%d\n%s%d\n%s%d\n%s%d\n%s%d\n" %(
                    "Number of students who received each grade:",
		    "A (90 - 100): ", self.__aCount,
		    "B (80 - 89): ", self.__bCount,
		    "C (70 - 79): ", self.__cCount,
		    "D (60 - 69): ", self.__dCount,
		    "F (Less than 60): ", self.__fCount))
        else:
            print("No grades were entered")
        
        
            
