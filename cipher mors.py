from tkinter import *
root= Tk()
root.geometry("500x500")
root.title("CIPHER MORS")
root.config(bg="#000080")
text1=Text(root,bg="black",fg="white",width=20,height=10)
text2=Text(root,bg="black",fg="green",width=20,height=10)
text1.place(x=100,y=50)
text2.place(x=100,y=260)

def chi():
    a=text1.get("1.0","end")
    c=list(a)
    for i in range(len(c)):
        if c[i]== "a":
            c[i]=".-"
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "b": 
            c[i] ="-..."
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "c":
            c[i]="-.-."
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "d":
            c[i]="-.."
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "e":
            c[i]="."
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "f":
            c[i]="..-."
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "g":
            c[i]="--."
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "h":
            c[i]="...."
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "i":
            c[i]=".."
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "j":
            c[i]=".---"
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "k":
            c[i]="-.-"
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "l":
            c[i]=".-.."
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "m":
            c[i]="--"
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "n":
            c[i]="-."
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "o":
            c[i]="---"
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "p":
            c[i]=".--."
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "q":
            c[i]="--.-"
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "r":
            c[i]=".-."
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "s":
            c[i]="..."
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "t":
            c[i]="-"
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "u":
            c[i]="..-"
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "v":
            c[i]="...-"
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "w":
            c[i]=".--"
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "x":
            c[i]="-..-"
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "y":
            c[i]="-.--"
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "z":
            c[i]="--.."
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "1":
            c[i]=".----"
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "2":
            c[i]="..---"
            w="".join(c[i])
            text2.insert(END,w)
        elif a[i]== "3":
            a[i]="...--"
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "4":
            c[i]="....-"
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "5":
            c[i]="....."
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "6":
            c[i]="-...."
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "7":
            c[i]="--..."
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "8":
            c[i]="---.."
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "9":
            c[i]="----."
            w="".join(c[i])
            text2.insert(END,w)
        elif c[i]== "0":
            c[i]="-----"
            w="".join(c[i])
            text2.insert(END,w)
        else:
            c[i]== ""
            c[i]="  "
            w="".join(c[i])
            text2.insert(END,w)
def de ():
    text1.delete("1.0","end")
    text2.delete("1.0","end")
        

b1=Button(root,text="trans",command=chi)
b2=Button(root,text="clear",command=de)
b1.place(x=130,y=220)
b2.place(x=200,y=220)
root.mainloop()