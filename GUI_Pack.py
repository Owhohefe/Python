import tkinter as tk

from tkinter import *

root = Tk()

root.geometry("100x200+30+30")

w = Label(root, text="Red", bg="red", fg="white")
w.pack(side=LEFT, padx = 10, pady = 10)
w = Label(root, text="Green", bg="green", fg="black")
w.pack(side=LEFT, padx = 10, pady = 10)
w = Label(root, text="Blue", bg="blue", fg="white")
w.pack(side=LEFT, padx = 10, pady = 10)

root.mainloop()
