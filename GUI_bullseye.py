import tkinter
from tkinter import *

root = Tk()

w = Canvas(root, width=250, height=250)

w.pack()

w.create_oval(250,250,10,10,fill="Yellow")
w.create_oval(220,220,40,40,fill="green")
w.create_oval(190,190,70,70,fill="Yellow")
w.create_oval(160,160,100,100,fill="green")

root.mainloop()
