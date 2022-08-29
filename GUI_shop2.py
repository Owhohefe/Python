import tkinter as tk

from tkinter import *

from tkinter.messagebox import *
    
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

def CheckOut():
    x = float(E4.get())
    root.destroy()

    def CheckPayment():
        y = float(CO_E2.get())
        if y == x:
            showinfo("Thanks", "Thanks for your patronage.\n\nYou can leave with the goods.")
            top.destroy()
        elif y > x:
            showinfo("Thanks", "Thanks for your patronage.\n\nTake your change of =N=%d.\n\nYou can leave with the goods."%(y-x))
            top.destroy()
        else:
            showerror("Sorry", "You have underpaid by =N=%d.\n\nPlease pay the correct amount"%(x-y))
            
    top = Tk()
    top.title("Check out")
    CO_L1 = Label(top, text="Total Cost of Goods:")
    CO_L2 = Label(top, text="Please enter the amount you are paying below:")
    CO_L3 = Label(top, text="Enter Amount:")
    
    CO_L1.grid(row = 0, column=0, columnspan=2)
    CO_L2.grid(row = 1, column=0, columnspan=3,sticky=W,pady= 10)
    CO_L3.grid(row = 2, column=0, sticky=W)

    CO_E1 = Entry(top)
    CO_E1.insert(10,x)
    CO_E1.config(state='readonly')

    CO_E2 = Entry(top)
    CO_E2.insert(10,"0.0")
    CO_E2.focus_set()
    
    CO_E1.grid(row = 0, column=2)
    CO_E2.grid(row = 2, column=2)

    CO_B1= Button(top, text="Click to Pay", command=CheckPayment)
    CO_B1.grid(row = 3, column=0, columnspan=3, pady= 10)
   
    
root = Tk()
root.title("Shop")
root.resizable(0,0)
#root.configure(background="#333")

#root.geometry("300x300+30+30")

chkValue = tk.BooleanVar()
chkValue.set(False)

chkValue1 = tk.BooleanVar()
chkValue1.set(False)

chkValue2 = tk.BooleanVar()
chkValue2.set(False)

C1 = Checkbutton(root, text="Shoe", command=ChangeState_C1, var=chkValue, font=('Arial', 10, 'bold'))
C2 = Checkbutton(root, text="Belt", command=ChangeState_C2, var=chkValue1,font=('Arial', 10, 'bold'))
C3 = Checkbutton(root, text="Bag", command=ChangeState_C3, var=chkValue2,font=('Arial', 10, 'bold'))

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
L4 = Label(root, text = "Price",font=('Arial', 12, 'bold'))
L5 = Label(root, text = "Quantity",font=('Arial', 12, 'bold'))
L6 = Label(root, text = "Total Cost of goods:",font=('Arial', 10, 'bold'))

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
B3 = Button(root, text="Check Out", command=CheckOut)

L4.grid(row = 1, column = 1, sticky=W, padx = 5)
L5.grid(row = 1, column = 2, sticky=W, padx = 5)
L6.grid(row = 5, column = 0,columnspan= 2, sticky=W, ipady=3)

C1.grid(row = 2, column = 0, sticky=W, ipady=3)
C2.grid(row = 3, column = 0, sticky=W, ipady=3)
C3.grid(row = 4, column = 0, sticky=W, ipady=3)

P1.grid(row = 2, column = 1, padx = 5, pady=5, sticky=W, ipady=3)
P2.grid(row = 3, column = 1, padx = 5, pady=5, sticky=W, ipady=3)
P3.grid(row = 4, column = 1, padx = 5, pady=5, sticky=W, ipady=3)

E1.grid(row = 2, column = 2 , padx = 5, pady=5, sticky=W, ipady=3)
E2.grid(row = 3, column = 2 , padx = 5, pady=5, sticky=W, ipady=3)
E3.grid(row = 4, column = 2 , padx = 5, pady=5, sticky=W, ipady=3)
E4.grid(row = 5, column = 2 , padx = 5, pady=5, sticky=W, ipady=3)

B1.grid(row = 6, column = 0,columnspan= 2, pady=5, ipadx=7, sticky=E, ipady=3)
B2.grid(row = 7, column = 0, columnspan= 3,pady=5, ipadx=7, ipady=3)
B3.grid(row = 6, column = 2, pady=5, ipadx=7, ipady=3)

root.mainloop()
