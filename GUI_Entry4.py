import tkinter as tk
from math import *

def evaluate(event):
    res.configure(text = "Result: " + str(eval(entry.get())))
    
w = tk.Tk()
tk.Label(w, text="Your Expression:").pack()
entry = tk.Entry(w, justify=tk.CENTER)
entry.bind('<Return>', evaluate)
entry.pack()
res = tk.Label(w)
res.pack()
w.mainloop()
