from tkinter import *
from tkinter.messagebox import *

root = Tk()

def getText(event):
    d = str(event.widget)
    if d == ".!entry":
        TEXT = E1.get()
        showinfo("Text", TEXT)
    elif d == ".!entry2":
        TEXT = E2.get()
        showinfo("Text", TEXT)
    elif d == ".!entry3":
        TEXT = E3.get()
        showinfo("Text", TEXT)
    elif d == ".!entry4":
        TEXT = E4.get()
        showinfo("Text", TEXT)

root.geometry("200x200+0+0")

E1 = Entry(root,width=10)
E1.pack()

E2 = Entry(root)
E2.insert(0,"Enter text here")
E2.pack()

E3 = Entry(root)
E3.insert(0,"Uneditable text field")
E3.config(state="readonly")
E3.pack()

E4 = Entry(root, show="*")
E4.insert(0,"Hidden Text")
E4.pack()

root.bind('<Return>', getText)

root.mainloop()
