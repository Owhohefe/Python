import tkinter as tk

from tkinter import *

root = Tk()

canvas_height = 200

canvas_width = 400

w = Canvas(root,height=canvas_height, width=canvas_width, bg="white")

w.create_rectangle(100,40,300,160,fill="green", width=3)

w.create_rectangle(130, 70, 270, 130,fill="yellow", width=3)

w.create_line(0,0,100,40,fill="green", width=3)

w.create_line(400,0,300,40,fill="green", width=3)

w.create_line(0,200,100,160,fill="green", width=3)

w.create_line(400,200,300,160,fill="green", width=3)

w.create_text(canvas_width / 2,
              canvas_height / 2,
              text="Python", font = "bold")

w.pack()

root.mainloop()
