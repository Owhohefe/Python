import tkinter as tk

from tkinter import *

root = Tk()

frame = Frame(root).pack()

v = IntVar()

Label(frame, text = """Choose a programming language:""", justify = LEFT, padx = 20).pack()

Radiobutton(frame, text = "Python", padx = 20, variable = v, value = 1).pack(anchor = W)

Radiobutton(frame, text = "Java", padx = 20, variable = v, value = 2).pack(anchor = W)

Radiobutton(frame, text = "Perl", padx = 20, variable = v, value = 3).pack(anchor = W)

root.mainloop()
