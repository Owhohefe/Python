import tkinter
from tkinter import *

root = Tk()

w = Canvas(root, width=500, height=250)

w.pack()

w.create_arc(460,460,10,10,start=0, extent=180,fill="red")
w.create_arc(430,430,40,40,start=0, extent=180,fill="orange")
w.create_arc(400,400,70,70,start=0, extent=180,fill="yellow")
w.create_arc(370,370,100,100,start=0, extent=180,fill="green")
w.create_arc(340,340,130,130,start=0, extent=180,fill="blue")
w.create_arc(310,310,160,160,start=0, extent=180,fill="indigo")
w.create_arc(280,280,190,190,start=0, extent=180,fill="violet")
w.create_arc(250,250,220,220,start=0, extent=180,fill="white")

root.mainloop()
