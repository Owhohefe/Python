from tkinter import *

from PIL import ImageTk

top = Tk()

C = Canvas(top, bg = "BLUE",height = 250, width = 300, bd = 7, cursor = "circle")

coord = 10, 50, 250, 210

arc = C.create_arc(coord, start=0, extent=150, fill="red")
line = C.create_line(10,10,200,200,fill='white')
oval = C.create_oval(10,10,200,200)
oval = C.create_polygon(10,10,200,200,250,100,100,100)

filename = PhotoImage(file = "pass.png")
image = C.create_image(200, 50, anchor=NE, image=filename)

C.pack()

top.mainloop()
