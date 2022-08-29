import tkinter

from tkinter import *

from tkinter.messagebox import *

class writeFile:

    def writeData(self):
        fhand = open(r"C:\Users\oekpom\Desktop\Python\RWFile.txt","a")
        fhand.write(E1.get())
        fhand.write("\n")
        E1.delete(0,'end')
        showinfo("Success","Data successfully saved to file")
        fhand.close()
        WF.readData()

    def readData(self):
        rhand = open(r"C:\Users\oekpom\Desktop\Python\RWFile.txt","r")
        data=rhand.readlines()
        if len(data)==1:
            text1.insert(INSERT,data[0])
        else:
            text1.insert(INSERT,data[-1])
        #text1.insert(INSERT,"\n")

WF = writeFile()

root = Tk()

root.geometry('400x400+100+100')

E1 = Entry(root,font=("verdana",15))

E1.place(x=30, y=40)

btn = Button(root, text="write",font=("verdana",10), command=WF.writeData)

btn.place(x=310, y=40)

text1 = Text(root, wrap=WORD, width=40, height=10)

text1.place(x=30, y=79)

root.mainloop()
