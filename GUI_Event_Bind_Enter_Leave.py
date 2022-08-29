import tkinter as tk

from tkinter import *

#import sys

def enter(event):
    T.delete(1.0, END)
    T.insert(END,("The mouse entered the widget at %s, %s!!" %(event.x, event.y)))
    msg.config(bg="yellow")
    
def leave(event):
    T.delete(1.0, END)
    T.insert(END,("The mouse left the widget!!"))
    msg.config(bg="lightgreen")
    
root = Tk()

whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"

msg = Message(root, text=whatever_you_do)
msg.config(bg="lightgreen", font=('times', 26, 'italic'))
msg.bind('<Enter>', enter)
msg.bind('<Leave>', leave)
msg.pack()

T = Text(root, height=1, width=40)
T.pack()
root.mainloop()
