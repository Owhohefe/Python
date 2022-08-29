from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk

root = Tk()
colorNames=["Black", "Blue", "Cyan","Dark Gray", "Gray", "Green",
            "Light Gray", "Magenta","Orange", "Pink", "Red", "White", "Yellow"]

def Copy():
    d = str(C4.get())
    T1.delete('1.0',END)
    T1.insert(END,d)
    
root.geometry("250x150+0+0")

C4 = ttk.Combobox(root, values=colorNames)
C4.place(relx=0.2,rely=0.1)

B1 = Button(root, text="Copy >>>", command=Copy)
B1.place(relx=0.4,rely=0.4)

T1 = Text(root,width=17,height=1)
T1.place(relx=0.2,rely=0.7)

root.mainloop()
