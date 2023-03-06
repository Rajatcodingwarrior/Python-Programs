from tkinter import *
import tkinter.messagebox as tmsg
import matplotlib.pyplot as plt

root=Tk()
root.geometry("380x400")
f1=Frame(root,bg="GREY")
Label(f1,text="Report Card",bg="RED",fg="black",font="lucida 20 bold",borderwidth=5,relief=SUNKEN).pack()
f1.pack(fill=X)
f2=Frame(root,bg="green")


a6=IntVar()
fr=f1=Frame(root,bg="red")
Label(fr,text="Grand Total",bg="magenta",fg="black",font="comicsansns 18 bold",borderwidth=5,relief=SUNKEN,padx=25).pack(side=LEFT)
Entry(fr,textvariable=a6,bg="white",fg="black",font="comicsansns 18 bold",borderwidth=5,relief=SUNKEN).pack(side=RIGHT)
fr.pack(fill=X)



Label(f2,text="Subject",bg="grey",fg="black",font="comicsansns 20 bold",borderwidth=5,relief=SUNKEN,padx=50).pack(side=LEFT)
Label(f2,text="Marks",bg="grey",fg="black",font="comicsansns 20 bold",borderwidth=5,relief=SUNKEN,padx=50).pack(side=LEFT)
f2.pack()

def t1():
    m=a1.get()+a2.get()+a3.get()+a4.get()+a5.get()
    n=int((m/a6.get())*100)
    tmsg.showinfo("RESULT",f"Total MARKS:{m},Percentage={n}")
    c=["English","IP","Maths","Physics","Chemistry"]
    r=[a1.get(),a2.get(),a3.get(),a4.get(),a5.get()]
    plt.xlabel("Subject",fontsize=20)
    plt.ylabel("Marks",fontsize=15)
    plt.title("Result",fontsize=20)
    plt.bar(c,r,color="red",width=0.8)
    plt.legend(["marks"])
    plt.show()


a1=IntVar()
a2=IntVar()
a3=IntVar()
a4=IntVar()
a5=IntVar()


f3=Frame(root,bg="green")
Label(f3,text="English",bg="grey",fg="black",font="comicsansns 20 bold",borderwidth=5,relief=SUNKEN,padx=50).pack(side=LEFT)
Entry(f3,textvariable=a1,bg="white",fg="black",font="comicsansns 20 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
f3.pack()


f4=Frame(root,bg="green")
Label(f4,text="IP",bg="grey",fg="black",font="comicsansns 20 bold",borderwidth=5,relief=SUNKEN,padx=86).pack(side=LEFT)
Entry(f4,textvariable=a2,bg="white",fg="black",font="comicsansns 20 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
f4.pack(side=TOP)


f5=Frame(root,bg="green")
Label(f5,text="Maths",bg="grey",fg="black",font="comicsansns 20 bold",borderwidth=5,relief=SUNKEN,padx=62).pack(side=LEFT)
Entry(f5,textvariable=a3,bg="white",fg="black",font="comicsansns 20 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
f5.pack(side=TOP)


f6=Frame(root,bg="green")
Label(f6,text="Physics",bg="grey",fg="black",font="comicsansns 20 bold",borderwidth=5,relief=SUNKEN,padx=48).pack(side=LEFT)
Entry(f6,textvariable=a4,bg="white",fg="black",font="comicsansns 20 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
f6.pack(side=TOP)

f7=Frame(root,bg="green")
Label(f7,text="Chemistry",bg="grey",fg="black",font="comicsansns 20 bold",borderwidth=5,relief=SUNKEN,padx=32).pack(side=LEFT)
Entry(f7,textvariable=a5,bg="white",fg="black",font="comicsansns 20 bold",borderwidth=5,relief=SUNKEN).pack(side=LEFT)
f7.pack(side=TOP)

f9=Frame(root,bg="blue")
Button(text="View Result",command=t1,bg="red",fg="black",font="comicsansns 20 bold",borderwidth=5,relief=SUNKEN,padx=30).pack(side=LEFT,anchor="n",padx=10)
Button(text="Exit",command=root.destroy,bg="red",fg="black",font="comicsansns 20 bold",borderwidth=5,relief=SUNKEN,padx=30).pack(side=LEFT,anchor="n",padx=10)
f9.pack(fil=X)

root.mainloop()
