from tkinter import *
from tkinter import ttk
import Login

class Chef_page(Tk):
  def __init__(self):
    super().__init__()
    
    self.geometry("%dx%d+0+0" % (self.winfo_screenwidth(), self.winfo_screenheight()))
    self.title("Maharaja Hotel Chef")
    self.wm_iconbitmap("Burger.ico")
    
    style_button = ttk.Style()
    style_button.configure("TButton",font = ("arial",10,"bold"),
    background="lightgreen")
    
    #================Title==============
    title_frame = Frame(self, bd=8, bg="yellow", relief=GROOVE)
    title_frame.pack(side=TOP, fill="x")
    
    logout_frame = Frame(title_frame, bg="yellow")
    logout_frame.pack(side='right')
    
    login_name = Label(logout_frame,text='CHEF',
                       font=("arial", 15, "bold"),bg = "yellow")
    login_name.grid(row=0,column=0)
    
    logout_button = ttk.Button(logout_frame, text="LOGOUT"
                            ,command=self.logout_operation)
    logout_button.grid(row=0,column=1,padx=10)
    
    title_label = Label(title_frame, text="Maharaja Hotel", 
                        font=("times new roman", 20, "bold"),bg = "yellow", fg="red", pady=5)
    title_label.pack()
    
    
  def logout_operation(self):
    self.destroy()
    self = Login.Login_page()
    
    
    
    
    
# For Test
if __name__=="__main__":
  root = Chef_page()
  root.mainloop()