from tkinter import *;
from tkinter import messagebox;

class CreateFile(object):
        #Rd=open('c:/TextFile/User.txt','r');
      def createFile(self):
        create=open('c:/TextFile/User.txt','w');
        create.write(txtbox.get());
        messagebox.showinfo("Success"," data has been written to "+create.name);
        return;
      def GetData(self):
          with open('c:/TextFile/User.txt','r') as Rd:
              gf=Rd.read();
              #messagebox.showinfo("FileRead",gf);
              SRead=Text(root,wrap=WORD, width=70, height=7, font=("cambria",40))
              SRead.insert(INSERT,gf)
              SRead.place(x=20,y=60)
      def center(self,w=300, h=100):
          ws=root.winfo_screenwidth();
          hs=root.winfo_screenheight();
          x=(ws/2)-(w/2);
          y=(hs/2)-(h/2)
          root.geometry('%dx%d+%d+%d' %(w,h,x,y))
C=CreateFile();




root=Tk()

txtbox=Entry(root, font=("verdana",12), bd=0.5);
txtbox.place(x=40,y=30)
btn=Button(root, text="Write", command=lambda:C.createFile())
btn.place(x=230,y=30)

#calling the center screen
C.center(500,200)
C.GetData();
root.mainloop();
