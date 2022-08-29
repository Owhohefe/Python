from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk

root = Tk()
colorNames=["Black", "Blue", "Cyan","Dark Gray", "Gray", "Green",
            "Light Gray", "Magenta","Orange", "Pink", "Red", "White", "Yellow"]

def ChangeState(event):
    d = str(C4.get())
    root.config(bg=d)
    
root.geometry("250x150+0+0")

C4 = ttk.Combobox(root, values=colorNames)
C4.bind("<<ComboboxSelected>>", ChangeState)
C4.pack()

root.mainloop()
