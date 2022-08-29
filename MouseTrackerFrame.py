from tkinter import *

root = Tk()

def mouseEntered(event):
    frame.config(bg="GREEN")
    label.config(text="Mouse Entered at [%d, %d]"%(event.x,event.y))

def mouseExited(event):
    frame.config(bg="WHITE")
    label.config(text="Mouse Exited at [%d, %d]"%(event.x,event.y))

def mouseClicked(event):
    label.config(text="Mouse Clicked at [%d, %d]"%(event.x,event.y))

def mouseMoved(event):
    label.config(text="Mouse Moved to [%d, %d]"%(event.x,event.y))

def mouseReleased(event):
    label.config(text="Mouse Released at [%d, %d]"%(event.x,event.y))

def mouseDoubleClicked(event):
    label.config(text="Mouse Clicked twice at [%d, %d]"%(event.x,event.y))
    
root.geometry("350x170+0+0")
root.title("Demonstrating Mouse Events")

frame = Frame(root,bg="WHITE", width=500,height=150)
frame.pack(fill=BOTH)

#<Button-1> is for left click
#<Button-2> is for the mouse wheel
#<Button-3> is for right click

frame.bind('<Enter>', mouseEntered)
frame.bind('<Leave>', mouseExited)
frame.bind("<Button-1>", mouseClicked)
frame.bind('<Motion>', mouseMoved)
frame.bind('<ButtonRelease-1>', mouseReleased)
frame.bind('<Double-Button-1>', mouseDoubleClicked)

label = Label(root,text="Mouse outside JPanel",bg="yellow")
label.pack(side=BOTTOM,fill=X)


root.mainloop()
