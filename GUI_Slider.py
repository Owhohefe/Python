import tkinter as tk

from tkinter import *

root = Tk()

root.title("Slider")

def getValues():
    print("Score 1= %s \nScore 2= %s" %(w.get(),w1.get()))

w = Scale(root, from_=0, to=40, tickinterval=2, length=150)

w.set(8)

w.pack()

w1 = Scale (root, from_=0, to=30, tickinterval=2, orient=HORIZONTAL, length=250)

w1.set(3)

w1.pack()

Button(root, text="Show", command=getValues).pack()

root.mainloop()
