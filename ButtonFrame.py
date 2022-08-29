from tkinter import *
from tkinter.messagebox import *

root = Tk()

def getText(event):
    d = str(event.widget)
    
    if d == ".!button":
        showinfo("Text","You clicked on the Plain Button")
    elif d == ".!button2":
        showinfo("Text","You clicked on the Fancy Button")

def enter(event):
    B2.config(image=img1)
    
def leave(event):
    B2.config(image=img)

root.geometry("200x200+0+0")

img = PhotoImage(file="add_bug.png")
img1 = PhotoImage(file="bug_insect.png")

B1 = Button(root, text="Plain Button")
B1.pack()

B2 = Button(root, text="Fancy Button", image=img, compound=LEFT, bg="white")
B2.bind('<Enter>', enter)
B2.bind('<Leave>', leave)
B2.pack()

root.bind("<Button-1>", getText)

root.mainloop()
