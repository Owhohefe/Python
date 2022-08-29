import tkinter as tk

from tkinter import *

from tkinter.filedialog import *

def callback():
    name = askopenfilename()
    print(name)

#errmsg = "Error!"
Button(text="Open File", command=callback).pack(fill=X)

mainloop()
