import tkinter as tk

from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300

w = Canvas(root, height = canvas_height, width = canvas_width)

img = PhotoImage(file="pass.png")

w.create_image(60,60,anchor=NW,image = img)

w.pack()

root.mainloop()
