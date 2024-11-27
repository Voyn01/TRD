from tkinter import *
import math 
from tkinter import messagebox
root= Tk()
root.geometry("500x500")
root.title("Калькулятор")
root.config(bg="#000000")
root.resizable(width=True,height=True)
x=Entry(root)
y=Entry(root)
r=Entry(root)
x.place(x=190,y=60)
y.place(x=190,y=110)
r.place(x=190,y=180)

#? function 
def att():
    messagebox.showerror(title=" warrning ",message=" Вы ошибались")

def plus():
    a=x.get()
    b=y.get()
    c=float(a) + float(b)
    r.insert(0,c)
    
def min ():
    a=x.get()
    b=y.get()
    c=float(a)- float(b)
    r.insert(0,c)
def mani():
    a=x.get()
    b=y.get()
    c=float(a) * float(b)
    r.insert(0,c)
    
         
def dev ():
    a=x.get()
    b=y.get()
    c=float(a) / float(b)
    r.insert(0,c)
   
def delet():
    x.delete(0,END)
    y.delete(0,END)
    r.delete(0,END)
#? buttons 
b1=Button(root ,text=" + ",command=plus,fg="red")
b2=Button(root ,text=" - ",command=min,fg="red")
b3=Button(root ,text=" / ",command=dev,fg="red")
b4=Button(root ,text=" * ",command=mani,fg="red")
b5=Button(root ,text=" c ",command=delet,fg="red")
l1=Label(root,text="Первый цифр" ,fg="red",bg="#000000")
l2=Label(root,text="Второй цифр" ,fg="red",bg="#000000")
l3=Label(root,text="Вывод" ,fg="red",bg="#000000")
l4=Label(root,text="КАЛЬКУЛЯТОР",bg='#000000',fg="white",font=100)
l1.place(x=190 ,y=40)
l2.place(x=190 ,y=90)
l3.place(x=190 ,y=160)
l4.place(x= 20,y=10  )
b1.place(x=360,y=60)
b2.place(x=360,y=90)
b3.place(x=360,y=120)
b4.place(x=360,y=150)
b5.place(x=360,y=180)


# if x==str():

#     l11=Label(root,text=" вы ошибались !!!")
#     l11.place(x=190,y=200)
# else:
#     prfloat("ok")
root.mainloop()