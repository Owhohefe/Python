import GradeBook3

from GradeBook3 import *

class GradeBook_3_Test:
    pass

gradesArray = [87,68,94,100,83,78,85,91,76,87]
gradesArray1 = [80,58,74,100,93,68,85,79,46,87]

GB3 = GradeBook3("Java Programming", gradesArray)
GB3.displayMessage()
GB3.processGrades()

print("\n\n***************************************************************")
GB4 = GradeBook3("Perl Programming", gradesArray1)
GB4.displayMessage()
GB4.processGrades()
