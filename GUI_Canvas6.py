import tkinter as tk

from tkinter import *

root = Tk()

canvas_width = 190
canvas_height =150

w = Canvas(root, height = canvas_height, width = canvas_width)

w.create_oval(0,95,190,115, fill="yellow")

w.pack()

root.mainloop()
