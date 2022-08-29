import tkinter

from tkinter import *

root = Tk()

root.geometry("250x250+100+100")

canvas = Canvas(root, height=250, width=250)

canvas.pack()

line = canvas.create_line(0,0,250,250,fill="black", width=3)

line2 = canvas.create_line(0,250,250,0,fill="black", width=3)

root.mainloop()
