from tkinter import *
root= Tk()
root.geometry("500x500")
root.title("Color Picker")
root.config(bg="#000000")


#*DOUBLEVAR


sd1=DoubleVar()
sd2=DoubleVar()
sd3=DoubleVar()
sd4=DoubleVar()
sd5=DoubleVar()


#*FUNCTION


def red(o=None):
    a=scl1.get()
    lb1.configure(bg="red")
def green(o=None):
    a=scl2.get()
    lb1.configure(bg="#00FF00")
def bleu(o=None):
    a=scl3.get()
    lb1.configure(bg="#0000FF")
def move(o=None):
    a=scl4.get()
    lb1.configure(bg="#800080")
def yelo(o=None):
    a=scl5.get()
    lb1.configure(bg="#FFFF00")

        
#*TITEL & SCAL

lb1=Label(root,text= "",width=20,height=10,bg="white")

scl1=Scale(root,label="",from_=0,to=10,variable=sd1,tickinterval=5,length=50,resolution=10,orient=HORIZONTAL,command=red,showvalue=0,fg="white",bg="#FF0000")
scl2=Scale(root,label="",from_=0,to=10,variable=sd2,tickinterval=5,length=50,resolution=10,orient=HORIZONTAL,command=green,showvalue=0,fg="white",bg="#00FF00")
scl3=Scale(root,label="",from_=0,to=10,variable=sd3,tickinterval=5,length=50,resolution=10,orient=HORIZONTAL,command=bleu,showvalue=0,fg="white",bg="#0000FF")
scl4=Scale(root,label="",from_=0,to=10,variable=sd4,tickinterval=5,length=50,resolution=10,orient=HORIZONTAL,command=move,showvalue=0,fg="white",bg="#800080")
scl5=Scale(root,label="",from_=0,to=10,variable=sd5,tickinterval=5,length=50,resolution=10,orient=HORIZONTAL,command=yelo,showvalue=0,fg="white",bg="#FFFF00")

lb1.place(x=231,y=120)
scl1.place(x=67,y=100)
scl2.place(x=67,y=160)
scl3.place(x=67,y=220)
scl4.place(x=67,y=280)
scl5.place(x=67,y=340)


root.mainloop()