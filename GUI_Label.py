import tkinter as tk

from tkinter import *

root = tk.Tk()

pic = PhotoImage(file="pass.png")

w1= Label(root, image=pic)

w1.pack(side="right")

explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""

w = Label(root, text=explanation, justify=LEFT,padx = 10)

w.pack(side="left")

root.mainloop()
