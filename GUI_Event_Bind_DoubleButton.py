import tkinter as tk

from tkinter import *

import sys

def motion(event):
    T.delete(1.0, END)
    T.insert(END,("Mouse position: (%s, %s)" % (event.x, event.y)))    
    
root = Tk()

whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"

msg = Message(root, text=whatever_you_do)
msg.config(bg="lightgreen", font=('times', 24, 'italic'))
msg.bind('<Double-Button-1>', motion)
msg.pack()

T = Text(root, height=1, width=36)
T.pack()
root.mainloop()
