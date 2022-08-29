import tkinter as tk

from tkinter import *

master = Tk()

var1 = IntVar()

var2 = IntVar()

def print_var():
    print("male: %s \nfemale: %s" % (var1.get(),var2.get()) )

Label(master, text="Choose your sex").grid(row=0, sticky=W)

Checkbutton(master, text="Male", variable=var1).grid(row=1, sticky=W)

Checkbutton(master, text="Female", variable=var2).grid(row=2, sticky=W)

Button(master, text="Quit", command=quit).grid(row = 3, sticky=W)

Button(master, text="Show", command=print_var).grid(row = 4, sticky=W)

master.mainloop()
