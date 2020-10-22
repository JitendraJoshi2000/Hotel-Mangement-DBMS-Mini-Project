from tkinter import *
from tkinter import ttk
import Login

class SignUp_page(Tk):
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
    
    back_button = ttk.Button(title_frame,text = "<<== Back",command=s.back_function)
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

    s.name = StringVar()
    s.name.set("")
    name_entry = Entry(signup_frame,width=20,font="arial 15",bd=5,
                                textvariable=s.name)
    name_entry.grid(row=0,column=1,pady=(10,10),padx=(10,0))
    
    #EmailId
    email_lable = Label(signup_frame,bg="lightgreen", text="Email Id", 
                    font=("arial", 15, "bold"), fg="blue")
    email_lable.grid(row=1,column=0,pady=(10,10))

    s.emailId = StringVar()
    s.emailId.set("")
    email_entry = Entry(signup_frame,width=20,font="arial 15",bd=5,
                                textvariable=s.emailId)
    email_entry.grid(row=1,column=1,pady=(10,10),padx=(10,0))
    
    # Phone No
    phone_lable = Label(signup_frame,bg="lightgreen", text="Phone No.", 
                    font=("arial", 15, "bold"), fg="blue")
    phone_lable.grid(row=2,column=0,pady=(10,10))

    s.phoneNo = StringVar()
    s.phoneNo.set("")
    phone_entry = Entry(signup_frame,width=20,font="arial 15",bd=5,
                                textvariable=s.phoneNo)
    phone_entry.grid(row=2,column=1,pady=(10,10),padx=(10,0))
    
    # Password
    password_lable = Label(signup_frame,bg="lightgreen", text="Password", 
                    font=("arial", 15, "bold"), fg="blue")
    password_lable.grid(row=3,column=0,pady=(10,10))

    s.password = StringVar()
    s.password.set("")
    password_entry = Entry(signup_frame,width=20,font="arial 15",bd=5,
                                textvariable=s.password)
    password_entry.grid(row=3,column=1,pady=(10,10),padx=(10,0))

    # Confirm Password
    confirm_password_lable = Label(signup_frame,bg="lightgreen", text="Confirm Password", 
                    font=("arial", 15, "bold"), fg="blue")
    confirm_password_lable.grid(row=4,column=0,pady=(10,10))

    s.confirm_password = StringVar()
    s.confirm_password.set("")
    confirm_password_entry = Entry(signup_frame,width=20,font="arial 15",bd=5,
                                textvariable=s.confirm_password)
    confirm_password_entry.grid(row=4,column=1,pady=(10,10),padx=(10,0))
    
    # Register
    register_button = ttk.Button(main_frame,text = "Register",command=s.register)
    register_button.pack(pady=(30,10))
  
  def back_function(s):
    s.destroy()
    s = Login.Login_page()  
  def register(s):
    print(s.name.get(),s.phoneNo.get(),s.emailId.get(),s.password.get())
    s.destroy()
    s = Login.Login_page()


'''
# For Test
if __name__=="__main__":
  root = SignUp_page('username','pass')
  root.mainloop()
  '''