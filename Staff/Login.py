from tkinter import *
from tkinter import ttk
import Admin,Waiter,Chef

class Login_page(Tk):
  def __init__(self):
    super().__init__()
    self.geometry("%dx%d+0+0" % (self.winfo_screenwidth(), self.winfo_screenheight()))
    self.title("Maharaja Hotel Staff Protal")
    self.wm_iconbitmap("Burger.ico")
    
    style_button = ttk.Style()
    style_button.configure("TButton",font = ("arial",10,"bold"),
    background="lightgreen")
    
    main_frame = Frame(self, bd=8, bg="lightgreen", relief=GROOVE)
    main_frame.pack(fill="both",expand=True)
    
    #================Title==============
    title_frame = Frame(main_frame, bd=8, bg="yellow", relief=GROOVE)
    title_frame.pack(side=TOP, fill="x")

    title_label = Label(title_frame, text="Maharaja Hotel Staff Protal", 
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
    
  def login(self):
    print(self.username.get(),self.password.get())
    username = self.username.get()
    password = self.password.get()
    if username=='admin' and password=='admin':
      self.destroy()
      self = Admin.Admin_page()
    elif username=='chef' and password=='chef':
      self.destroy()
      self = Chef.Chef_page()
    elif username=='waiter' and password=='waiter':
      # Get Data from database
      self.destroy()
      self = Waiter.Waiter_page(username)
      #s = Customer.Customer_page(username,password)
    else:
      tmsg.showinfo("Error", "Wrong Username or password")
    
    
'''
# For Test
if __name__=="__main__":
  root = Login_page()
  root.mainloop()
  '''