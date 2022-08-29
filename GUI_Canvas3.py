import tkinter as tk

from tkinter import *

root = Tk()

canvas_height = 40

canvas_width = 80

w = Canvas(root,height=canvas_height, width=canvas_width, bg="black")

w.pack()

y = int(canvas_height / 2)

w.create_line(0,y,80,y,fill="white")

root.mainloop()
