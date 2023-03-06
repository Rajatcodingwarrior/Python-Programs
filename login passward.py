from tkinter import*
from PIL import ImageTk
class login_system:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN SYSTEM")
        self.root.geometry("1600x820+0+0")
        self.bg_icon=ImageTk.PhotoImage(file="images/bg.jpg")
        self.user_icon=PhotoImage(file="images/username.png")
        self.pass_icon=PhotoImage(file="images/passward.png")

        title=Label(self.root,text="Login Systems",font=("times new roman",40,"bold"))
        title.place(x=0,y=0,erlwidth=1)

root=Tk()
object=login_system(root)
root.mainloop()
