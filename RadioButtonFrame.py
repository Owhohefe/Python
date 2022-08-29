from tkinter import *
from tkinter.messagebox import *

root = Tk()

def ChangeState():
    if var.get()==4:
        T1.config(font=('Arial', 10, 'bold', 'italic'))
        
    elif var.get()==2:
        T1.config(font=('Arial', 10, 'bold'))

    elif var.get()==3:
        T1.config(font=('Arial', 10, 'italic'))

    elif var.get()==1:
        T1.config(font=('Arial', 10))

var = IntVar()
var.set(1)

root.geometry("250x150+0+0")

T1 = Text(root, width=27, height=1,font=('Arial', 10))
T1.insert(END,"Watch the font style change")
T1.pack(anchor=W)

R1 = Radiobutton(root, text="Plain", variable = var, value=1, command=ChangeState)
R1.pack(anchor=W)

R2 = Radiobutton(root, text="Bold", variable = var, value=2, command=ChangeState)
R2.pack(anchor=W)

R3 = Radiobutton(root, text="Italic", variable = var, value=3, command=ChangeState)
R3.pack(anchor=W)

R4 = Radiobutton(root, text="Bold/Italic", variable = var, value=4, command=ChangeState)
R4.pack(anchor=W)

root.mainloop()
