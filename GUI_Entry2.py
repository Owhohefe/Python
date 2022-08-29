import tkinter as tk

from tkinter import *

root = Tk()
root.title("Entry")

def show_entry():
    print("First Name: %s \nLast Name: %s" %(E1.get(), E2.get()))
    E1.delete(0, END)
    E2.delete(0, END)
    
Label(root, text="First Name:").grid(row=0, column=0)
Label(root, text="Last Name:").grid(row=1, column=0)

E1 = Entry(root)
E2 = Entry(root)

#E1.insert(10, "Miller")
#E2.insert(10, "Jill")

E1.grid(row=0, column=1)
E2.grid(row=1, column=1)

Button(root, text="Show", command=show_entry).grid(row=2, column=0)
Button(root, text="Quit", command=quit).grid(row=2, column=1)

root.mainloop()
