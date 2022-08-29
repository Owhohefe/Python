from tkinter import *

from tkinter.colorchooser import askcolor

root = Tk()

color = "BLACK"

def ChooseColor():
    global color
    result = askcolor(color="white", title= "Bernd's Colour Chooser")
    color = result[1]
    
def paint(event):
    x1,y1 = event.x-1, event.y-1
    x2,y2 = event.x+1, event.y+1
    canvas.create_oval(x1,y1,x2,y2,fill = color,outline = color)
    
root.geometry("350x170+0+0")
root.title("Drawing on a canvas")

canvas = Canvas(root,bg="WHITE", width=500, height=150)
canvas.pack(fill=BOTH)

#<Button-1> is for left click
#<Button-2> is for the mouse wheel
#<Button-3> is for right click

canvas.bind('<B1-Motion>', paint)

label = Label(root, text="Press and Drag the mouse to draw", bg="BLACK", fg="WHITE")
label.pack(side=BOTTOM,fill=X)

M = Menu(root)
root.config(menu = M)
paletteMenu = Menu(M)
M.add_cascade(label="Palette", menu=paletteMenu)
paletteMenu.add_cascade(label="Choose Color", command=ChooseColor)

root.mainloop()
