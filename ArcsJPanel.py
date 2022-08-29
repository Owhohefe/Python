import tkinter
from tkinter import *

root = Tk()

w = Canvas(root, width=315, height=180)

w.pack()

w.create_rectangle(15, 35, 100, 100,outline="red")

w.create_arc(15, 35, 100, 100,start=0, extent=359,outline="black",style="arc")


w.create_rectangle(120, 35, 200, 100,outline="red")

w.create_arc(120, 35, 200, 100,start=0, extent=90,outline="black",style="arc")


w.create_rectangle(225, 35, 300, 100,outline="red")

w.create_arc(225, 35, 300, 100,start=0, extent=-270,outline="black",style="arc")


w.create_arc(15, 150, 100, 110,start=0, extent=359, fill="black")

w.create_arc(120, 150, 200, 110,start=270, extent=-90, fill="black")

w.create_arc(225, 150, 300, 110,start=0, extent=-270, fill="black")


root.mainloop()
