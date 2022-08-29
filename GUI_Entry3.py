import tkinter as tk

from tkinter import *

root = Tk()
root.title("Loan Calculator")

def monthly_payment():
    # period rate:
    r = (float(E1.get()) / 100) / 12
    print("r", r)
    # principal loan:
    loan = float(E3.get())
    n =  float(E2.get())
    remaining_loan = float(E5.get())
    q = (1 + r)** n
    monthly = r * ( (q * loan - remaining_loan) / ( q - 1 ))
    monthly = ("%8.2f" % monthly).strip()
    E4.delete(0, tk.END)
    E4.insert(0, monthly)
    print("Monthly Payment: %f" % float(monthly))

def final_balance():
    # period rate:
    r = (float(E1.get()) / 100) / 12
    print("r", r)
    # principal loan:
    loan = float(E3.get())
    n =  float(E2.get()) 
    monthly = float(E4.get())
    q = (1 + r) ** n
    remaining = q * loan  - ( (q - 1) / r) * monthly
    remaining = ("%8.2f" % remaining).strip()
    E5.delete(0, tk.END)
    E5.insert(0, remaining )
    print("Remaining Loan: %f" % float(remaining))
    
Label(root, text="Annual Rate:",width=18,anchor=W).grid(row=0, column=0)
Label(root, text="Number of Payments:", width=18,anchor=W).grid(row=1, column=0)
Label(root, text="Loan Principal:", width=18,anchor=W).grid(row=2, column=0)
Label(root, text="Monthly Payment:", width=18,anchor=W).grid(row=3, column=0)
Label(root, text="Remaining Loan:",width=18,anchor=W).grid(row=4, column=0)

E1 = Entry(root, justify=CENTER)
E2 = Entry(root, justify=CENTER)
E3 = Entry(root, justify=CENTER)
E4 = Entry(root, justify=CENTER)
E5 = Entry(root, justify=CENTER)

E1.insert(10,"0.00")
E2.insert(10,"0.00")
E3.insert(10,"0.00")
E4.insert(10,"0.00")
E5.insert(10,"0.00")

E1.grid(row=0, column=1)
E2.grid(row=1, column=1)
E3.grid(row=2, column=1)
E4.grid(row=3, column=1)
E5.grid(row=4, column=1)

Button(root, text="Final Balance", command=final_balance,width=13).grid(row=5, column=0,sticky=W)
Button(root, text="Monthly Payment", command=monthly_payment, width=13).grid(row=5, column=1, sticky=W)
Button(root, text="Quit", command=quit, width=13).grid(row=5, column=2, sticky=W)

root.mainloop()
