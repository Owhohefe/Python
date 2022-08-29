import tkinter as tk

from tkinter import *

root = tk.Tk()

root.title("Test")

text = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"

m = Message(root, text = text)

m.config(bg = "lightgreen", font = ("Helvetica", 24, "italic"), justify = LEFT, takefocus = "true")

m.pack()

root.mainloop()
