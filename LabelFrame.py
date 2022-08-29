from tkinter import *

root = Tk()

root.geometry("400x400+0+0")

L1 = Label(root, text="Label with text").pack()

img = PhotoImage(file="C:\\Users\\oekpom\\Desktop\\Python\\pass.png")
L2 = Label(root, image = img, text="Label with text and icon",compound=LEFT).pack()

L3 = Label(root, image = img, text="Label with icon and text at bottom",compound=TOP).pack()

root.mainloop()
