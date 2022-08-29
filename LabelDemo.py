import tkinter
from tkinter import *

root = Tk()

root.geometry("400x400+100+100")

L1 = Label(root, text="North")
L1.pack(side=TOP)

img = PhotoImage(file="C:\\Users\\oekpom\\Desktop\\python\\pass.png")
L2 = Label(root, image=img)
L2.pack()

L3 = Label(root, image=img, text="South")
L3.pack(side=BOTTOM)

L4 = Label(root,text="South")
L4.pack()

root.mainloop()
