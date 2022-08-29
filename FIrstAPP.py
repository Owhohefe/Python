from tkinter import *;


def center_window(w=300, h=400):
    ws=top.winfo_screenwidth()
    hs=top.winfo_screenheight()
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)
    top.geometry('%dx%d+%d+%d' % (w,h,x,y))

top=Tk()
top.resizable(0,0)
top.configure(background="#333")
top.title("Home Screen");

for r in range(5):
    for c in range (5):
        Label(top, text="%s/%s"%(r,c)).grid(row=r, column=c)
        
btn=Button(top, text="Click Me", bg="forestgreen", fg="white",height=10, width=10);
btn.place(x=100,y=200)
center_window(800, 500);
top.mainloop();
