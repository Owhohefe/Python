import tkinter as tk

from tkinter import *

def ChangeState_C1():
    if chkValue.get()==True:
        E1.config(state='normal')
        E1.delete(0, END)
        E1.focus_set()
    else:
        E1.insert(10,"0")
        E1.config(state='readonly')
        
def ChangeState_C2():
    if chkValue1.get()==True:
        E2.config(state='normal')
        E2.delete(0, END)
        E2.focus_set()
    else:
        E2.insert(10,"0")
        E2.config(state='readonly')

def ChangeState_C3():
    if chkValue2.get()==True:
        E3.config(state='normal')
        E3.delete(0, END)
        E3.focus_set()
    else:
        E3.insert(10,"0")
        E3.config(state='readonly')

def ComputeCost():
    x = ((float(E1.get())*float(P1.get('1.0', END)))+(float(E2.get())*float(P2.get('1.0', END)))+(float(E3.get())*float(P3.get('1.0', END))))
    E4.config(state='normal')
    E4.delete(0, END)
    E4.insert(10,x)
    E4.config(state='readonly')

    
root = Tk()
root.title("Shop")
root.resizable(0,0)
#root.configure(background="#333")

#root.geometry("200x200+30+30")

chkValue = tk.BooleanVar()
chkValue.set(False)

chkValue1 = tk.BooleanVar()
chkValue1.set(False)

chkValue2 = tk.BooleanVar()
chkValue2.set(False)

C1 = Checkbutton(root, text="Shoe", command=ChangeState_C1, var=chkValue)
C2 = Checkbutton(root, text="Belt", command=ChangeState_C2, var=chkValue1)
C3 = Checkbutton(root, text="Bag", command=ChangeState_C3, var=chkValue2)

P1 = Text(root, height=1 , width = 5)
P2 = Text(root, height=1 , width = 5)
P3 = Text(root, height=1 , width = 5)

P1.insert(END,"6500")
P2.insert(END,"1000")
P3.insert(END,"2500")

P1.config(state=DISABLED)
P2.config(state=DISABLED)
P3.config(state=DISABLED)

#L1 = Label(root, text = "Shoe")
#L2 = Label(root, text = "Belt")
#L3 = Label(root, text = "Bag")
L4 = Label(root, text = "Price")
L5 = Label(root, text = "Quantity")
L6 = Label(root, text = "Total Cost of goods:")

E1 = Entry(root)
E2 = Entry(root)
E3 = Entry(root)
E4 = Entry(root)

E1.insert(10,"0")
E2.insert(10,"0")
E3.insert(10,"0")
E4.insert(10,"0.0")

E1.config(state='readonly')
E2.config(state='readonly')
E3.config(state='readonly')
E4.config(state='readonly')

B1 = Button(root, text="Compute Cost", command=ComputeCost)
B2 = Button(root, text="Exit", command=quit)


L4.grid(row = 1, column = 1, sticky=W, padx = 5)
L5.grid(row = 1, column = 2, sticky=W, padx = 5)
L6.grid(row = 5, column = 0,columnspan= 2, sticky=W)

C1.grid(row = 2, column = 0, sticky=W)
C2.grid(row = 3, column = 0, sticky=W)
C3.grid(row = 4, column = 0, sticky=W)

P1.grid(row = 2, column = 1, padx = 5, pady=5, sticky=W)
P2.grid(row = 3, column = 1, padx = 5, pady=5, sticky=W)
P3.grid(row = 4, column = 1, padx = 5, pady=5, sticky=W)

E1.grid(row = 2, column = 2 , padx = 5, pady=5, sticky=W)
E2.grid(row = 3, column = 2 , padx = 5, pady=5, sticky=W)
E3.grid(row = 4, column = 2 , padx = 5, pady=5, sticky=W)
E4.grid(row = 5, column = 2 , padx = 5, pady=5, sticky=W)

B1.grid(row = 6, column = 0,columnspan= 2, pady=5, ipadx=7, sticky=E)
B2.grid(row = 6, column = 2, pady=5, ipadx=7)


root.mainloop()
