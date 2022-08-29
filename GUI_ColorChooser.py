import tkinter as tk

from tkinter import *

from tkinter.colorchooser import askcolor

def callback():
    result = askcolor(color="white", title= "Bernd's Colour Chooser")
    #print(result)
    T.config(bg=result[1])

root = Tk()

T = Text(root, height = 4, width = 30, bg = "red")

T.pack()

Button(root, text="Choose Colour", fg = "darkgreen", command=callback).pack(side=LEFT, padx=10)

Button(root, text="Quit", fg = "red", command=quit).pack(side=LEFT, padx=10)

root.mainloop()
