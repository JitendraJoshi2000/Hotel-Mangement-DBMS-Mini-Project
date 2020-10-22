from tkinter import *
from tkinter import ttk
import SignUp
import Customer

class Login_page(Tk):
  def __init__(s):
    super().__init__()
    s.geometry("%dx%d+0+0" % (s.winfo_screenwidth(), s.winfo_screenheight()))
    s.title("Welcome to Maharaja Hotel")
    s.wm_iconbitmap("Burger.ico")
    
    style_button = ttk.Style()
    style_button.configure("TButton",font = ("arial",10,"bold"),
    background="lightgreen")
    
    main_frame = Frame(s, bd=8, bg="lightgreen", relief=GROOVE)
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

    s.username = StringVar()
    s.username.set("")
    username_entry = Entry(login_frame,width=20,font="arial 15",bd=5,
                                textvariable=s.username)
    username_entry.grid(row=0,column=1,padx=(10,0))
    
    # Password
    password_lable = Label(login_frame,bg="lightgreen", text="Password", 
                    font=("arial", 15, "bold"), fg="blue")
    password_lable.grid(row=1,column=0,pady=(50,10))

    s.password = StringVar()
    s.password.set("")
    password_entry = Entry(login_frame,show="*",width=20,font="arial 15",bd=5,
                                textvariable=s.password)
    password_entry.grid(row=1,column=1,pady=(50,10),padx=(10,0))


    login_button = ttk.Button(main_frame,text = "LOGIN",command=s.login)
    login_button.pack(pady=30)
    
    #================Sign Up==============
    signUp_frame = Frame(main_frame,bg='lightgreen',bd=10)
    signUp_frame.pack(fill="y",expand=False)
    
    signUp_lable = Label(signUp_frame,bg="lightgreen", text="Not Registered?", 
                    font=("arial", 15, "bold"), fg="blue")
    signUp_lable.grid(row=0,column=0,pady=(30,10))
    
    register_button = ttk.Button(signUp_frame,text = "Sign Up Here",command=s.signup)
    register_button.grid(row=0,column=1,pady=(30,10))
    
  def signup(s):
    s.destroy()
    s = SignUp.SignUp_page()
    
  def login(s):
    print(s.username.get(),s.password.get())
    username = s.username.get()
    password = s.password.get()
    s.destroy()
    s = Customer.Customer_page(username,password)
    
    
'''
# For Test
if __name__=="__main__":
  root = Login_page()
  root.mainloop()
  '''