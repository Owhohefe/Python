from tkinter import *
from tkinter.messagebox import *

root = Tk()

def ChangeState():
    if chkValue.get()==True and chkValue1.get()==True:
        T1.config(font=('Arial', 10, 'bold', 'italic'))
        
    elif chkValue.get() == True and chkValue1.get()==False:
        T1.config(font=('Arial', 10, 'bold'))

    elif chkValue.get() == False and chkValue1.get()==True:
        T1.config(font=('Arial', 10, 'italic'))

    else:
        T1.config(font=('Arial', 10))

chkValue = BooleanVar()
chkValue.set(False)

chkValue1 = BooleanVar()
chkValue1.set(False)

root.geometry("250x100+0+0")

T1 = Text(root, width=27, height=1,font=('Arial', 10))
T1.insert(END,"Watch the font style change")
T1.pack()

C1 = Checkbutton(root, text="Bold", variable=chkValue, command=ChangeState)
C1.pack()

C2 = Checkbutton(root, text="Italic", variable=chkValue1, command=ChangeState)
C2.pack()

root.mainloop()
