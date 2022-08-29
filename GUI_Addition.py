from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

root = Tk()

root.withdraw()

firstNum = simpledialog.askinteger("Input", "Enter an Integer",minvalue=0, maxvalue=100)

secondNum = simpledialog.askinteger("Input", "Enter an Integer",minvalue=0, maxvalue=100)

result = firstNum + secondNum

messagebox.showinfo("Result","The sum of the 2 Integers is %d"%(result))

root.mainloop()
