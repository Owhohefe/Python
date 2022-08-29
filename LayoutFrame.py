from tkinter import *

def left():
    frame.pack(side=LEFT)

def center():
    frame.place(x=70, y=0)

def right():
    frame.pack(side=RIGHT)
    
root = Tk()
root.title("Layout Demo")

root.geometry("400x100+100+100")

frame = Frame(root,width=250, height = 100, bg="GREEN")
frame.pack()

leftButton = Button(frame,text="LEFT",command=left)
leftButton.place(relx=0.1, rely=0.4)

centerButton = Button(frame,text="CENTER", command=center)
centerButton.place(relx=0.36, rely=0.4)

rightButton = Button(frame,text="RIGHT", command=right)
rightButton.place(relx=0.7, rely=0.4)


root.mainloop()
