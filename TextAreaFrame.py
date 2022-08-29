import tkinter as tk

from tkinter import *

root = Tk()

def copy():
    T1.delete('1.0', END)
    try:
        T1.insert(END,T.selection_get())
    except:
        pass
    

root.geometry("500x80+100+100")

root.title("Text")

T = Text(root, height=5, width=20)

scroll = Scrollbar(root, command=T.yview)

T.configure(yscrollcommand=scroll.set)

T.pack(side=LEFT, fill=Y)

scroll.pack(side=LEFT, fill=Y)

quote = "This is a demo string to illustrate copying text from one textarea to another textarea using an external event";

T.insert(END,quote)


T1 = Text(root, height=5, width=20)

scroll2 = Scrollbar(root, command=T1.yview)

T1.configure(yscrollcommand=scroll2.set)

scroll2.pack(side=RIGHT, fill=Y)

T1.pack(side=RIGHT, fill=Y)

B1 = Button(root, text="Copy>>>", command=copy)

B1.place(x=220, y=40)

root.mainloop()



