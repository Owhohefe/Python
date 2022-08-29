from tkinter import *

import tkinter

from tkinter import messagebox

top = tkinter.Tk()

CheckVar1 = IntVar()

CheckVar2 = IntVar()

def PlayMusic ():
    msg = messagebox.showinfo("Playing music","USHER")

def PlayVideo ():
    msg = messagebox.showinfo("Playing Video","GOT")  

C1 = Checkbutton(top, text = "Music", variable = CheckVar1, onvalue = 1, offvalue = 0, height = 5, width = 20, command = PlayMusic)

C2 = Checkbutton(top, text = "Video", variable = CheckVar2, onvalue = 1, offvalue = 0, height = 5, width = 20, command = PlayVideo)

C1.pack(side = LEFT)

C2.pack(side = LEFT)

top.mainloop()
