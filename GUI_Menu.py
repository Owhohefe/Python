import tkinter as tk

from tkinter import *

from tkinter.filedialog import askopenfilename

def NewFile():
    print("New file")
def OpenFile():
    result = askopenfilename()
    print("result")
def about():
    print("This is a simple example of a menu")


root = Tk()
M = Menu(root)
root.config(menu=M)
filemenu = Menu(M)
M.add_cascade(label="File", menu=filemenu)
filemenu.add_cascade(label="New", command=NewFile)
filemenu.add_separator()
filemenu.add_cascade(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_cascade(label="Exit", command=quit)

helpmenu = Menu(M)
M.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_cascade(label="About", command=about)

root.mainloop()
