import tkinter as tk

from tkinter import *

import sys

def hello(event):
    print("Single Click, Button-1")

def quit(event):
    print("Double Click, so lets stop")
    sys.exit()

w = Button(None, text="Mouse Clicks")
w.pack()

w.bind("<Button-1>", hello)
w.bind("<Double-1>", quit)

w.mainloop()
