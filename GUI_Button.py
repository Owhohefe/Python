from tkinter import *

from tkinter import messagebox

top = Tk()

top.geometry("200x200")

def helloCallBack():
    msg = messagebox.showinfo("TEST","Hello World")

B = Button(top, text = "Hello", command = helloCallBack, bd = 6, fg = "YELLOW", font = "SERIF", height = 1, highlightcolor = "BLUE", width = 8, underline = 0)

B.place(x=50, y=100)

B.invoke()

top.mainloop()
