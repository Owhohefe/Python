import tkinter as tk

from tkinter import *

master = Tk()

var1 = IntVar()

var2 = IntVar()

def print_var():
    print(var1.get())

def print_var2():
    print(var2.get())

CB1 = Checkbutton(master, text="Male", variable=var1, command=print_var).grid(row=0, sticky=W)

CB2 = Checkbutton(master, text="Female", variable=var2, command=print_var2).grid(row=1, sticky=W)

master.mainloop()
