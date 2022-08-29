import tkinter

from tkinter import *

root = Tk()

root.geometry("400x400+100+100")

C = Canvas(root, height=400, width=400)

choice = int(input("Enter 1 for Rectangle and 2 for Oval: "))

if choice == 1:

    for i in range(10):
    
        C.create_rectangle(10+i*10,10+i*10,50+i*10,50+i*10,width=i)
        C.create_oval(10+i*10,10+i*10,50+i*10,50+i*10,width=i)

elif choice == 2:

    for i in range(10):
    
        C.create_oval(10+i*10,10+i*10,50+i*10,50+i*10,width=i)   

C.pack()

root.mainloop()

    
