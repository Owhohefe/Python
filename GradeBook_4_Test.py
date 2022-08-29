import GradeBook4

from GradeBook4 import *

class GradeBook_4_Test:
    pass


gradesArray = [[87,96,70],[68,87,90],[94,100,90],[100,81,82],[83,65,85],[78,87,65],[85,75,83],[91,94,100],[76,72,84],[87,93,73]]

GB3 = GradeBook4("Java Programming", gradesArray)
GB3.displayMessage()
GB3.processGrades()

print("\n\n***************************************************************")
GB4 = GradeBook4("Perl Programming", gradesArray)
GB4.displayMessage()
GB4.processGrades()
