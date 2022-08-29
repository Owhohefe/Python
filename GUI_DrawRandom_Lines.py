from tkinter import *
import random

top = Tk()

C = Canvas(top, bg = "white", height = 300, width = 300, bd = 7, cursor = "circle")

C.pack()

dimension = []
count = 5 + random.randint(0,5)

for i in range(count):
    coord = random.randint(0,300), random.randint(0,300), random.randint(0,300), random.randint(0,300)
    dimension.append(coord)
    
colors = ["blue","green","orange","purple","yellow","brown","red","black","purple"]

for j in dimension:
    C.create_line(j,fill=random.choice(colors))

top.mainloop()
