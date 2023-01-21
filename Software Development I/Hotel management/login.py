from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from hotel import HotelManagementSystem


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1366x768+0+0")

        # variables 
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"E:\Academic\5th semester\Software Development I\Hotel management - Copy\images\hotel5.jpg")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1, relheight=1)

        frame1= Frame(self.root,bg="#ccd1d1")
        frame1.place(x=560,y=170,width=340,height=450)

        img1=Image.open(r"E:\Academic\5th semester\Software Development I\Hotel management - Copy\images\hotel1.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lb1img1=Label(image=self.photoimage1,bg="#DAF7A6")
        lb1img1.place(x=690,y=170, width=100,height=100)

        get_str = Label(frame1,text="Hotel Management System",font=("times new roman",16,"bold"),fg="white",bg="#800000")
        get_str.place(x=45,y=100)
        

        #label1 
        username =lb1= Label(frame1,text="Username:",font=("times new roman",15,"bold"),fg="white",bg="#800000")
        username.place(x=30,y=160)

        #entry1 
        self.txtuser=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtuser.place(x=33,y=190,width=270)


        #label2 
        pwd =lb1= Label(frame1,text="Password:",font=("times new roman",15,"bold"),fg="white",bg="#800000")
        pwd.place(x=30,y=230)

        #entry2 
        self.txtpwd=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=33,y=260,width=270)


        # Creating Button Login
        loginbtn=Button(frame1,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#800000",bg="white",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=33,y=320,width=270,height=35)

    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")

        elif (self.txtuser.get() != self.txtpwd.get()):
            messagebox.showerror("Error","Wrong Password or Username!")

        elif(self.txtuser.get()=="admin" and self.txtpwd.get()=="admin"):
           
            self.new_window = Toplevel(self.root)
            self.app = HotelManagementSystem(self.new_window)

# ==================Funtion for Open Images Folder==================
    # def open_img(self):
    #     os.startfile("data_img")

if __name__ == "__main__":
    root=Tk()
    app=Login(root)
    root.mainloop()