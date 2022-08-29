from tkinter import *

root = Tk()

count = 1
count1 = 1
count2 = 1

def mouseEntered(event):
    frame.config(bg="GREEN")
    label.config(text="Mouse Entered at [%d, %d]"%(event.x,event.y))

def mouseExited(event):
    frame.config(bg="YELLOW")
    label.config(text="Mouse Exited at [%d, %d]"%(event.x,event.y))
    global count
    global count1
    global count2
    count = 1
    count1 = 1
    count2 = 1

def mouseMoved(event):
    label.config(text="Mouse Moved to [%d, %d]"%(event.x,event.y))
    global count
    global count1
    global count2
    count = 1
    count1 = 1
    count2 = 1
    
def leftMouseClick(event):
    global count
    global count1
    global count2
    
    count1 = 1
    count2 = 1
    
    if count == 1:
        label.config(text="Clicked %d time with the left mouse button"%(count))
    else:
        label.config(text="Clicked %d times with the left mouse button"%(count))
    count = count + 1

def RightMouseClick(event):
    global count
    global count1
    global count2
    
    count = 1
    count2 = 1
    
    if count1 == 1:
        label.config(text="Clicked %d time with the right mouse button"%(count1))
    else:
        label.config(text="Clicked %d times with the right mouse button"%(count1))
    count1 = count1 + 1

def MouseWheelClick(event):
    global count
    global count1
    global count2
    
    count = 1
    count1 = 1
    
    if count2 == 1:
        label.config(text="Clicked %d time with the mouse wheel button"%(count2))
    else:
        label.config(text="Clicked %d times with the mouse wheel button"%(count2))
    count2 = count2 + 1
    
root.geometry("350x170+0+0")
root.title("Demonstrating Mouse Events")

frame = Frame(root,bg="YELLOW", width=500,height=150)
frame.pack(fill=BOTH)

#<Button-1> is for left click
#<Button-2> is for the mouse wheel
#<Button-3> is for right click

frame.bind('<Enter>', mouseEntered)
frame.bind('<Leave>', mouseExited)
frame.bind('<Motion>', mouseMoved)
frame.bind("<Button-1>", leftMouseClick)
frame.bind("<Button-2>", MouseWheelClick)
frame.bind("<Button-3>", RightMouseClick)

label = Label(root, text="Mouse outside Frame", bg="BLACK", fg="WHITE")
label.pack(side=BOTTOM,fill=X)

root.mainloop()
