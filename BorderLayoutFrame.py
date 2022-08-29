from tkinter import *

def hidenorth():
    northButton.pack_forget()
    bottomButton.pack(side=BOTTOM, fill= X)
    leftButton.pack(side=LEFT, fill= Y)
    rightButton.pack(side=RIGHT, fill= Y)

def hidebottom():
    bottomButton.pack_forget()
    northButton.pack(side=TOP, fill= X)
    leftButton.pack(side=LEFT, fill= Y)
    rightButton.pack(side=RIGHT, fill= Y)

def hideleft():
    leftButton.pack_forget()
    northButton.pack(side=TOP, fill= X)
    bottomButton.pack(side=BOTTOM, fill= X)
    rightButton.pack(side=RIGHT, fill= Y)

def hideright():
    rightButton.pack_forget()
    northButton.pack(side=TOP, fill= X)
    bottomButton.pack(side=BOTTOM, fill= X)
    leftButton.pack(side=LEFT, fill= Y)
    
root = Tk()

root.title("Layout Demo")

root.geometry("300x200+100+100")

northButton = Button(root,text="Hide North", command=hidenorth)
northButton.pack(side=TOP, fill= X)

##centerButton = Button(root,text="Hide Center")
##centerButton.pack(anchor=CENTER)

bottomButton = Button(root,text="Hide South",command=hidebottom)
bottomButton.pack(side=BOTTOM, fill= X)

leftButton = Button(root,text="Hide East", command=hideleft)
leftButton.pack(side=LEFT, fill= Y)

rightButton = Button(root,text="Hide West", command=hideright)
rightButton.pack(side=RIGHT, fill= Y)


root.mainloop()
