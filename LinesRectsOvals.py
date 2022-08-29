from tkinter import *

top = Tk()

def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):

    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]

    return C.create_polygon(points, **kwargs, smooth=True)

C = Canvas(top, bg="WHITE",height=180, width=410)

C.create_line(10,10,400,10,fill='RED')
C.create_rectangle(10,20,100,80,outline="Blue")
C.create_rectangle(115,20,200,80,outline="Blue",fill="Blue")
round_rectangle(215,20,300,80,radius=20,outline="blue",fill="white")
round_rectangle(315,20,400,80,radius=20,outline="blue",fill="blue")

C.create_rectangle(10,105,100,160,outline="GREEN")
C.create_rectangle(115,105,200,160,outline="GREEN",fill="GREEN")

C.create_oval(215,105,300,160,outline="MAGENTA")
C.create_oval(315,105,400,160,outline="MAGENTA",fill="MAGENTA")

C.pack()

top.mainloop()
