from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Login
import re
import sqlite3

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

class SignUp_page(Tk):
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
    
    back_button = ttk.Button(title_frame,text = "<<== Back",command=self.back_function)
    back_button.pack(side=LEFT)

    title_label = Label(title_frame, text="Maharaja Hotel", 
                    font=("times new roman", 20, "bold"),bg = "yellow", fg="red", pady=5)
    title_label.pack()
    #================Sign Up==============
    signup_lable = Label(main_frame,bg="lightgreen", text="Sign Up", 
                    font=("arial", 15, "bold"), fg="red")
    signup_lable.pack(pady=(50,10))
    
    signup_frame = Frame(main_frame,bg='lightgreen',bd=10)
    signup_frame.pack(fill="y",expand=False)

    #================Customer Info==============
    #Name
    name_lable = Label(signup_frame,bg="lightgreen", text="Name", 
                    font=("arial", 15, "bold"), fg="blue")
    name_lable.grid(row=0,column=0,pady=(10,10))

    self.name = StringVar()
    self.name.set("")
    name_entry = Entry(signup_frame,width=20,font="arial 15",bd=5,
                                textvariable=self.name)
    name_entry.grid(row=0,column=1,pady=(10,10),padx=(10,0))
    
    #EmailId
    email_lable = Label(signup_frame,bg="lightgreen", text="Email Id", 
                    font=("arial", 15, "bold"), fg="blue")
    email_lable.grid(row=1,column=0,pady=(10,10))

    self.emailId = StringVar()
    self.emailId.set("")
    email_entry = Entry(signup_frame,width=20,font="arial 15",bd=5,
                                textvariable=self.emailId)
    email_entry.grid(row=1,column=1,pady=(10,10),padx=(10,0))
    
    # Phone No
    phone_lable = Label(signup_frame,bg="lightgreen", text="Phone No.", 
                    font=("arial", 15, "bold"), fg="blue")
    phone_lable.grid(row=2,column=0,pady=(10,10))

    self.phoneNo = StringVar()
    self.phoneNo.set("")
    phone_entry = Entry(signup_frame,width=20,font="arial 15",bd=5,
                                textvariable=self.phoneNo)
    phone_entry.grid(row=2,column=1,pady=(10,10),padx=(10,0))
    
    # Password
    password_lable = Label(signup_frame,bg="lightgreen", text="Password", 
                    font=("arial", 15, "bold"), fg="blue")
    password_lable.grid(row=3,column=0,pady=(10,10))

    self.password = StringVar()
    self.password.set("")
    password_entry = Entry(signup_frame,show="*",width=20,font="arial 15",bd=5,
                                textvariable=self.password)
    password_entry.grid(row=3,column=1,pady=(10,10),padx=(10,0))

    # Confirm Password
    confirm_password_lable = Label(signup_frame,bg="lightgreen", text="Confirm Password", 
                    font=("arial", 15, "bold"), fg="blue")
    confirm_password_lable.grid(row=4,column=0,pady=(10,10))

    self.confirm_password = StringVar()
    self.confirm_password.set("")
    confirm_password_entry = Entry(signup_frame,show="*",width=20,font="arial 15",bd=5,
                                textvariable=self.confirm_password)
    confirm_password_entry.grid(row=4,column=1,pady=(10,10),padx=(10,0))
    
    # Register
    register_button = ttk.Button(main_frame,text = "Register",command=self.register)
    register_button.pack(pady=(30,10))
  
  def back_function(self):
    self.destroy()
    self = Login.Login_page() 

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
      
    if flag ==-1: 
        return True

  def check_fields(self):
    if self.name.get()=="" or self.phoneNo.get()=="" or self.emailId.get()=="" or self.password.get()=="" or self.confirm_password.get()=="":
      messagebox.showerror("input","Please enter all fields!")
      return True
    elif not self.phoneNo.get().isdigit():
      messagebox.showerror("phone","Please enter valid Phone Number!")
      return True
    elif self.check_email(self.emailId.get()):
      messagebox.showerror("email","Please enter valid Email Address!")
      return True
    elif self.check_password(self.password.get()):
      messagebox.showerror("password","Password field should contain atleast one lowercase letter,uppercase letter,digit and one special charater")
      return True
    elif self.password.get()!=self.confirm_password.get():
      messagebox.showerror("confirm_password","Password and Confirm Password fields should match!")
      return True
    else:
      db = sqlite3.connect('../hotel_database.db')
      cursor = db.cursor()
      cursor.execute(f"insert into Customer values('{self.emailId.get()}','{self.name.get()}','{self.phoneNo.get()}','{self.password.get()}');")
      # cursor.execute("delete from Customer;")
      db.commit()
      return False

  def register(self):
    # print(self.name.get(),self.phoneNo.get(),self.emailId.get(),self.password.get())
    if self.check_fields():
      return
    self.destroy()
    self = Login.Login_page()

'''
# For Test
if __name__=="__main__":
  root = SignUp_page('username','pass')
  root.mainloop()
  '''