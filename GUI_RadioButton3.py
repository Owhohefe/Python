import tkinter as tk

from tkinter import *

root = Tk()

v = IntVar()

v.set(0)

languages = {
    "Python":1,
    "Perl":2,
    "Java":3,
    "C++":4,
    "C":5}

def showChoice():
    print (v.get())

Label(root, text="""Choose your favourite programming language:""", justify = LEFT, padx =20).pack()

for language, val in languages.items():
    Radiobutton(root, text = language, padx = 20, variable = v, command=showChoice, value = val).pack(anchor=W)

root.mainloop()
