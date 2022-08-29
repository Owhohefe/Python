import tkinter as tk

from tkinter import *

import sys

def focusIn(event):
    T.delete(1.0, END)
    T.insert(END,("The widget is focused on!!"))
    T.config(bg="lightgreen")

def focusOut(event):
    T.delete(1.0, END)
    T.insert(END,("Focus left the widget!!"))
    T.config(bg="white")
    
root = Tk()

T = Text(root, height=5, width=36)
T1 = Text(root, height=5, width=36)
T.bind('<FocusIn>', focusIn)
T.bind('<FocusOut>', focusOut)
T.pack()
T1.pack()
root.mainloop()
