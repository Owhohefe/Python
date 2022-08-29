import tkinter as tk

from tkinter import *

root = Tk()

#root.geometry("200x200+30+30")

L1 = Label(root, text = "Height")
L2 = Label(root, text = "Width")

L1.grid(row = 0, column = 0)

L2.grid(row = 1, column = 0)

E1 = Entry(root)
E2 = Entry(root)

E1.grid(row = 0, column = 1)
E2.grid(row = 1, column = 1)

C = Checkbutton(root, text="Preserve")

C.grid(row = 2, column = 0, columnspan = 2, sticky=W)

def Attach():
    img = PhotoImage(file = r"C:\Users\oekpom\Desktop\Python\pass.png")
    img1 = img.subsample(3,3)
    self.L3 = Label(root, image = img1)

L3.grid(row = 0, column=2, columnspan=2, rowspan=2)

B1 = Button(root, text = "Zoom in", command=Attach)
B2 = Button(root, text = "Zoom out")

B1.grid(row = 2, column=2)

B2.grid(row = 2, column=3)

root.mainloop()
