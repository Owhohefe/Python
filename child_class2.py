import parent_class2

import child_class3

from parent_class2 import add_numbers

from child_class3 import divide_numbers

class child_class(divide_numbers, add_numbers):
            
    def multiply(self):
        u = cc.x * cc.a * cc.y
        print(u)
          
cc = child_class()
cc.multiply()
cc.divide()
cc.add()

