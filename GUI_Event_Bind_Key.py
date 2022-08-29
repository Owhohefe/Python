import tkinter as tk

from tkinter import *

def Key_Press(event):
    T.insert(END,("The user pressed a key"))  
    
root = Tk()

T = Text(root, height=10, width=36)
T.bind('<Key>', Key_Press)
T.pack()
root.mainloop()
