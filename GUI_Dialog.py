import tkinter as tk

from tkinter import *

from tkinter.messagebox import *

def answer():
    showerror("Answer", "Sorry, no answer available")

def callback():
    if askyesno("verify", "Really quit?"):
        showwarning("yes", "Not yet implemented")
    else:
        showinfo("No", "Quit has been cancelled")

Button(text="Quit", command=callback).pack(fill=X)
Button(text="Answer", command=answer).pack(fill=X)

mainloop()
