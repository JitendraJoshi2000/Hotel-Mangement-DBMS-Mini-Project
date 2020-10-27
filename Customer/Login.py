from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import SignUp
import Customer
import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

class Login_page(Tk):
  def __init__(self):
    super().__init__()
    self.geometry("%dx%d+0+0" % (self.winfo_screenwidth(), self.winfo_screenheight()))
    self.title("Welcome to Maharaja Hotel")
    self.wm_iconbitmap("Burger.ico")
    
    style_button = ttk.Style()
    style_button.configure("TButton",font = ("arial",10,"bold"),
    background="lightgreen")
    
    main_frame = Frame(self, bd=8, bg="lightgreen", relief=GROOVE)
    main_frame.pack(fill="both",expand=True)
    
    #================Title==============
    title_frame = Frame(main_frame, bd=8, bg="yellow", relief=GROOVE)
    title_frame.pack(side=TOP, fill="x")

    title_label = Label(title_frame, text="Maharaja Hotel", 
                    font=("times new roman", 20, "bold"),bg = "yellow", fg="red", pady=5)
    title_label.pack()
    #================Login==============
    login_lable = Label(main_frame,bg="lightgreen", text="Login", 
                    font=("arial", 15, "bold"), fg="red")
    login_lable.pack(pady=(50,10))
    
    login_frame = Frame(main_frame,bg='lightgreen',bd=10)
    login_frame.pack(fill="y",expand=False)

    # Username
    username_lable = Label(login_frame,bg="lightgreen", text="Username", 
                    font=("arial", 15, "bold"), fg="blue")
    username_lable.grid(row=0,column=0)

    self.username = StringVar()
    self.username.set("")
    username_entry = Entry(login_frame,width=20,font="arial 15",bd=5,
                                textvariable=self.username)
    username_entry.grid(row=0,column=1,padx=(10,0))
    
    # Password
    password_lable = Label(login_frame,bg="lightgreen", text="Password", 
                    font=("arial", 15, "bold"), fg="blue")
    password_lable.grid(row=1,column=0,pady=(50,10))

    self.password = StringVar()
    self.password.set("")
    password_entry = Entry(login_frame,show="*",width=20,font="arial 15",bd=5,
                                textvariable=self.password)
    password_entry.grid(row=1,column=1,pady=(50,10),padx=(10,0))


    login_button = ttk.Button(main_frame,text = "LOGIN",command=self.login)
    login_button.pack(pady=30)
    
    #================Sign Up==============
    signUp_frame = Frame(main_frame,bg='lightgreen',bd=10)
    signUp_frame.pack(fill="y",expand=False)
    
    signUp_lable = Label(signUp_frame,bg="lightgreen", text="Not Registered?", 
                    font=("arial", 15, "bold"), fg="blue")
    signUp_lable.grid(row=0,column=0,pady=(30,10))
    
    register_button = ttk.Button(signUp_frame,text = "Sign Up Here",command=self.signup)
    register_button.grid(row=0,column=1,pady=(30,10))
    
  def signup(self):
    self.destroy()
    self = SignUp.SignUp_page()

  def check_email(self, email): 
    if(re.search(regex,email)):  
        return False    
    else:  
        return True  
    
  def check_password(self, password):
    flag = 0
    while True:   
        if (len(password)<8): 
            flag = -1
            break
        elif not re.search("[a-z]", password): 
            flag = -1
            break
        elif not re.search("[A-Z]", password): 
            flag = -1
            break
        elif not re.search("[0-9]", password): 
            flag = -1
            break
        elif not re.search("[_@$]", password): 
            flag = -1
            break
        elif re.search("\s", password): 
            flag = -1
            break
        else: 
            flag = 0
            return False 
            break
      
    if flag ==-1: 
        return True

  def check_fields(self):
    if self.username.get()=="" or self.password.get()=="":
      messagebox.showerror("input","Please enter all fields!")
      return True
    elif self.check_email(self.username.get()):
      messagebox.showerror("email","Please enter valid Email Address!")
      return True
    elif self.check_password(self.password.get()):
      messagebox.showerror("password","Password field should contain atleast one lowercase letter,uppercase letter,digit and one special charater!")
      return True
    return False
    
  def login(self):
    # print(self.username.get(),self.password.get())
    if self.check_fields():
      return
    username = self.username.get()
    password = self.password.get()
    self.destroy()
    self = Customer.Customer_page(username,password)
    
    
'''
# For Test
if __name__=="__main__":
  root = Login_page()
  root.mainloop()
  '''