from tkinter import *
from tkinter import ttk
import Login

class Admin_page(Tk):
  def __init__(s):
    super().__init__()
    
    s.geometry("%dx%d+0+0" % (s.winfo_screenwidth(), s.winfo_screenheight()))
    s.title("Maharaja Hotel Admin")
    s.wm_iconbitmap("Burger.ico")
    
    style_button = ttk.Style()
    style_button.configure("TButton",font = ("arial",10,"bold"),
    background="lightgreen")
    
    #================Title==============
    title_frame = Frame(s, bd=8, bg="yellow", relief=GROOVE)
    title_frame.pack(side=TOP, fill="x")
    
    logout_frame = Frame(title_frame, bg="yellow")
    logout_frame.pack(side='right')
    
    login_name = Label(logout_frame,text='ADMIN',
                       font=("arial", 15, "bold"),bg = "yellow")
    login_name.grid(row=0,column=0)
    
    logout_button = ttk.Button(logout_frame, text="LOGOUT"
                            ,command=s.logout_operation)
    logout_button.grid(row=0,column=1,padx=10)
    
    title_label = Label(title_frame, text="Maharaja Hotel", 
                        font=("times new roman", 20, "bold"),bg = "yellow", fg="red", pady=5)
    title_label.pack()
    
    
  def logout_operation(s):
    s.destroy()
    s = Login.Login_page()
    
    
    
    
    
# For Test
if __name__=="__main__":
  root = Admin_page()
  root.mainloop()