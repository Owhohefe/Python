import tkinter as tk

from tkinter import *

import sys

def Return(event):
    T.insert(END,("The user pressed the enter key"))  
    
root = Tk()

T = Text(root, height=10, width=36)
T.bind('<Return>', Return)
T.pack()
root.mainloop()
