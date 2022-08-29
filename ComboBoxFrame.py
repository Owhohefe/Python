from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk

root = Tk()
names=["bug_insect.png","add_bug.png","ladybird.png","insect.png"]
icons = [PhotoImage(file=names[0]),PhotoImage(file=names[1]),PhotoImage(file=names[2]),PhotoImage(file=names[3])]

def ChangeState(event):
    d = str(C4.get())
    
    if d =="bug_insect.png":
        L1.config(image=icons[0])
        
    elif d =="add_bug.png":
        L1.config(image=icons[1])

    elif d =="ladybird.png":
        L1.config(image=icons[2])
        
    elif d =="insect.png":
        L1.config(image=icons[3])

root.geometry("200x150+0+0")

C4 = ttk.Combobox(root, values=names)
C4.bind("<<ComboboxSelected>>", ChangeState)
C4.pack(side=LEFT)

L1 = Label(root,image=icons[1])
L1.pack(side=LEFT)                                                                       
#root.bind('<Return>', ChangeState)
#root.bind('<Button-1>', ChangeState)


root.mainloop()
