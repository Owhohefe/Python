import tkinter

from tkinter import *

from tkinter.messagebox import *

class TextFile():

    def SaveData(self):
        F = open("StudentData.txt", "a")

        Entry =[E1.get(),E2.get(),E3.get(),E4.get()]

        for i in Entry:
            F.write(i+" ")
        F.write("\n")
        
        F.close()
        
        E1.delete(0,'end')
        E2.delete(0,'end')
        E3.delete(0,'end')
        E4.delete(0,'end')

        showinfo("Success", "The information was successfully saved to file")

        
TF = TextFile()


top = Tk()

L0 = Label(top,text="Registration form:", font=("Serif",16,"bold"))
L1 = Label(top,text="First Name:", font=("Serif",14))
L2 = Label(top,text="Last Name:", font=("Serif",14))
L3 = Label(top,text="Course:", font=("Serif",14))
L4 = Label(top,text="MAT. No:", font=("Serif",14))

E1 = Entry(top)
E2 = Entry(top)
E3 = Entry(top)
E4 = Entry(top)

B1 = Button(top, text="Save", command=TF.SaveData)
B2 = Button(top, text="Exit", command=quit)

L0.grid(row=0, column=0,columnspan=2 ,sticky=W, pady=10)
L1.grid(row=1, column=0,pady=4, sticky=W)
L2.grid(row=2, column=0,pady=4, sticky=W)
L3.grid(row=3, column=0,pady=4, sticky=W)
L4.grid(row=4, column=0,pady=4, sticky=W)

E1.grid(row=1, column=1,pady=4, sticky=W, padx=7)
E2.grid(row=2, column=1,pady=4, sticky=W, padx=7)
E3.grid(row=3, column=1,pady=4, sticky=W, padx=7)
E4.grid(row=4, column=1,pady=4, sticky=W, padx=7)

B1.grid(row=5, column=0, padx=7, pady=15, ipadx=10)
B2.grid(row=5, column=1, padx=7, pady=15, ipadx=10)

top.mainloop()
