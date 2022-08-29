import tkinter as tk

from tkinter import *

def write_slogan():
    print("tkinter is easy to use")

root = tk.Tk()

frame = Frame(root)

frame.pack()

b1 = Button(frame, text="QUIT", fg = "red", command = quit)

b1.pack(side = LEFT)

b2 = Button(frame, text="HELLO", fg = "GREEN", command = write_slogan)

b2.pack(side = LEFT)

root.mainloop()
