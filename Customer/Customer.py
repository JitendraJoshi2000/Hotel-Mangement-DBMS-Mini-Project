from tkinter import *
from tkinter import ttk
import Login
import os

class Customer_page(Tk):
  def __init__(self,emailId,password):
    super().__init__()
    self.geometry("%dx%d+0+0" % (self.winfo_screenwidth(), self.winfo_screenheight()))
    self.title(f"Welcome to Maharaja Hotel, Customer {emailId}, {password}")
    self.wm_iconbitmap("Burger.ico")

    style_button = ttk.Style()
    style_button.configure("TButton",font = ("arial",10,"bold"),background="lightgreen")
  
    self.customerEmail = emailId
    self.customerpassword = password

    #================Title==============
    title_frame = Frame(self, bd=8, bg="yellow", relief=GROOVE)
    title_frame.pack(side=TOP, fill="x")
    
    logout_frame = Frame(title_frame, bg="yellow")
    logout_frame.pack(side='right')
    
    login_name = Label(logout_frame,text=emailId,
                       font=("arial", 15, "bold"),bg = "yellow")
    login_name.grid(row=0,column=0)
    
    logout_button = ttk.Button(logout_frame, text="LOGOUT"
                            ,command=self.logout_operation)
    logout_button.grid(row=0,column=1,padx=10)
    
    title_label = Label(title_frame, text="Maharaja Hotel", 
                        font=("times new roman", 20, "bold"),bg = "yellow", fg="red", pady=5)
    title_label.pack()
    
    #===============Menu===============
    menu_frame = Frame(self,bd=8, bg="lightgreen", relief=GROOVE,width=(self.winfo_screenwidth()//2))
    menu_frame.pack(side='left',fill='both')
    
    menu_label = Label(menu_frame, text="Menu", 
                        font=("times new roman", 18, "bold"),bg = "lightgreen", fg="red", pady=0)
    menu_label.pack(side=TOP,fill="x")
    
    menu_category_frame = Frame(menu_frame,bg="lightgreen",pady=10)
    menu_category_frame.pack(fill="x")
    
    combo_lable = Label(menu_category_frame,text="Select Type", 
                        font=("arial", 12, "bold"),bg = "lightgreen", fg="blue")
    combo_lable.grid(row=0,column=0,padx=10)
    
    self.menuCategory = StringVar()
    menu_category = ["Tea & Coffee","Beverages","Fast Food","South Indian","Starters","Main Course","Dessert"]

    menu_category_dict = {"Tea & Coffee":"1 Tea & Coffee.txt","Beverages":"2 Beverages.txt",
                "Fast Food":"3 Fast Food.txt","South Indian":"4 South Indian.txt",
                "Starters":"5 Starters.txt","Main Course":"6 Main Course.txt",
                "Dessert":"7 Dessert.txt"}

    order_dict = {}
    for i in menu_category:
        order_dict[i] = {}
    combo_menu = ttk.Combobox(menu_category_frame,values=menu_category,
                                textvariable=self.menuCategory)
    combo_menu.grid(row=0,column=1,padx=30)
    
    show_button = ttk.Button(menu_category_frame, text="Show",width=10,
                            command=self.show_button_operation)
    show_button.grid(row=0,column=2,padx=60)
    
    show_all_button = ttk.Button(menu_category_frame, text="Show All",
                            width=10,command=self.load_menu)
    show_all_button.grid(row=0,column=3,padx=(10,50))
    
    ############################# Menu Tabel ##########################################
    menu_tabel_frame = Frame(menu_frame,bd=2, relief=SUNKEN)
    menu_tabel_frame.pack(fill=BOTH,expand=1)
    
    scrollbar_menu_x = Scrollbar(menu_tabel_frame,orient=HORIZONTAL)
    scrollbar_menu_y = Scrollbar(menu_tabel_frame,orient=VERTICAL)
    
    style = ttk.Style()
    style.configure("Treeview.Heading",font=("arial",13, "bold"))
    style.configure("Treeview",font=("arial",12),rowheight=25)
    
    self.menu_tabel = ttk.Treeview(menu_tabel_frame,style = "Treeview",
                columns =("name","price","category"),xscrollcommand=scrollbar_menu_x.set,
                yscrollcommand=scrollbar_menu_y.set)
    
    self.menu_tabel.heading("name",text="Name")
    self.menu_tabel.heading("price",text="Price")
    self.menu_tabel["displaycolumns"]=("name", "price")
    self.menu_tabel["show"] = "headings"
    self.menu_tabel.column("price",width=50,anchor='center')
    
    scrollbar_menu_x.pack(side=BOTTOM,fill=X)
    scrollbar_menu_y.pack(side=RIGHT,fill=Y)
    
    scrollbar_menu_x.configure(command=self.menu_tabel.xview)
    scrollbar_menu_y.configure(command=self.menu_tabel.yview)
    
    self.menu_tabel.pack(fill=BOTH,expand=1)
    
    
    #menu_tabel.insert('',END,values=["Masala Dosa","50"])
    self.load_menu()
    self.menu_tabel.bind("<ButtonRelease-1>",self.load_item_from_menu)
    
    ###########################################################################################
    
    #===============Item Frame=============
    item_frame = Frame(self,bd=8, bg="lightgreen", relief=GROOVE)
    item_frame.pack(fill='x',anchor=SE)
    
    item_title_label = Label(item_frame, text="Item", 
                        font=("times new roman", 18, "bold"),bg = "lightgreen", fg="red")
    item_title_label.pack(side=TOP,fill="x")
    
    item_frame2 = Frame(item_frame, bg="lightgreen")
    item_frame2.pack(fill=X)
    
    item_name_label = Label(item_frame2, text="Name", 
                        font=("arial", 12, "bold"),bg = "lightgreen", fg="blue")
    item_name_label.grid(row=0,column=0,padx=(30,10))
    
    itemCategory = StringVar()
    itemCategory.set("")
    
    itemName = StringVar()
    itemName.set("")
    item_name = Entry(item_frame2, font="arial 12",textvariable=itemName,state=DISABLED, width=25)
    item_name.grid(row=0,column=1,padx=(0,10))
    
    item_rate_label = Label(item_frame2, text="Rate", 
                        font=("arial", 12, "bold"),bg = "lightgreen", fg="blue")
    item_rate_label.grid(row=0,column=2,padx=(40,10))
    
    itemRate = StringVar()
    itemRate.set("")
    item_rate = Entry(item_frame2, font="arial 12",textvariable=itemRate,state=DISABLED, width=10)
    item_rate.grid(row=0,column=3,padx=0)
    
    item_quantity_label = Label(item_frame2, text="Quantity", 
                        font=("arial", 12, "bold"),bg = "lightgreen", fg="blue")
    item_quantity_label.grid(row=1,column=0,padx=(30,0),pady=15)
    
    itemQuantity = StringVar()
    itemQuantity.set("")
    item_quantity = Entry(item_frame2, font="arial 12",textvariable=itemQuantity, width=10)
    item_quantity.grid(row=1,column=1,padx=0)
    
    item_frame3 = Frame(item_frame, bg="lightgreen")
    item_frame3.pack(fill=X)
    
    add_button = ttk.Button(item_frame3, text="Add Item"
                            ,command=self.add_button_operation)
    add_button.grid(row=0,column=0,padx=(40,25),pady=30)
    
    remove_button = ttk.Button(item_frame3, text="Remove Item"
                            ,command=self.remove_button_operation)
    remove_button.grid(row=0,column=1,padx=25,pady=30)
    
    update_button = ttk.Button(item_frame3, text="Update Quantity"
                            ,command=self.update_button_operation)
    update_button.grid(row=0,column=2,padx=25,pady=30)
    
    clear_button = ttk.Button(item_frame3, text="Clear",
                            width=8,command=self.clear_button_operation)
    clear_button.grid(row=0,column=3,padx=25,pady=30)
    
    #==============Order Frame=====================
    order_frame = Frame(self,bd=8, bg="lightgreen", relief=GROOVE)
    order_frame.pack(fill='both',anchor=SE,expand=True)
    
    order_title_label = Label(order_frame, text="Your Order", 
                        font=("times new roman", 18, "bold"),bg = "lightgreen", fg="red")
    order_title_label.pack(side=TOP,fill="x")
    
    ############################## Order Tabel ###################################
    order_tabel_frame = Frame(order_frame, bd=2, relief=SUNKEN)
    order_tabel_frame.pack(fill='x')
    
    scrollbar_order_x = Scrollbar(order_tabel_frame,orient=HORIZONTAL)
    scrollbar_order_y = Scrollbar(order_tabel_frame,orient=VERTICAL)
    
    order_tabel = ttk.Treeview(order_tabel_frame,
                columns =("name","rate","quantity","price","category"),xscrollcommand=scrollbar_order_x.set,
                yscrollcommand=scrollbar_order_y.set)
    
    order_tabel.heading("name",text="Name")
    order_tabel.heading("rate",text="Rate")
    order_tabel.heading("quantity",text="Quantity")
    order_tabel.heading("price",text="Price")
    order_tabel["displaycolumns"]=("name", "rate","quantity","price")
    order_tabel["show"] = "headings"
    order_tabel.column("rate",width=100,anchor='center', stretch=NO)
    order_tabel.column("quantity",width=100,anchor='center', stretch=NO)
    order_tabel.column("price",width=100,anchor='center', stretch=NO)
    
    order_tabel.bind("<ButtonRelease-1>",self.load_item_from_order)
    
    scrollbar_order_x.pack(side=BOTTOM,fill=X)
    scrollbar_order_y.pack(side=RIGHT,fill=Y)
    
    scrollbar_order_x.configure(command=order_tabel.xview)
    scrollbar_order_y.configure(command=order_tabel.yview)
    
    order_tabel.pack(fill=BOTH,expand=1)
    
    # order_tabel.insert('',END,text="HEllo",values=["Masala Dosa","50","2","100"])
    ###########################################################################################
    
    total_price_label = Label(order_frame, text="Total Price", 
                        font=("arial", 12, "bold"),bg = "lightgreen", fg="blue")
    total_price_label.pack(side='left',anchor=N,padx=(20,5),pady=20)
    
    totalPrice = StringVar()
    totalPrice.set("")
    total_price_entry = Entry(order_frame, font="arial 12",textvariable=totalPrice,state=DISABLED, 
                                width=10)
    total_price_entry.pack(side='left',anchor=N,padx=0,pady=20)
    
    bill_button = ttk.Button(order_frame, text="Place Order",
                            command=self.bill_button_operation)
    bill_button.pack(side='left',anchor=N,padx=50,pady=20)
    
    cancel_button = ttk.Button(order_frame, text="Delete Order",command=self.cancel_button_operation)
    cancel_button.pack(side='left',anchor=N,padx=0,pady=20)
    
    #====================Frontend code ends=====================
        

  def show_button_operation(self):
    return
    
  def load_menu(self):
    self.menuCategory.set("")
    self.menu_tabel.delete(*self.menu_tabel.get_children())
    menu_file_list = os.listdir("Menu")
    for file in menu_file_list:
        f = open("Menu\\" + file , "r")
        category=""
        while True:
            line = f.readline()
            if(line==""):
                self.menu_tabel.insert('',END,values=["","",""])
                break
            elif (line=="\n"):
                continue
            elif(line[0]=='#'):
                category = line[1:-1]
                name = "\t\t"+line[:-1]
                price = ""
            elif(line[0]=='*'):
                name = line[:-1]
                price = ""
            else:
                name = line[:line.rfind(" ")]
                price = line[line.rfind(" ")+1:-3]
            
            self.menu_tabel.insert('',END,values=[name,price,category])
        #menu_tabel.insert('',END,values=["Masala Dosa","50"])

  def load_item_from_menu(self):
    return

  def add_button_operation(self):
    return

  def remove_button_operation(self):
    return

  def update_button_operation(self):
    return

  def clear_button_operation(self):
    return

  def load_item_from_order(self):
    return

  def bill_button_operation(self):
    return

  def cancel_button_operation(self):
    return
  
  def logout_operation(self):
    self.destroy()
    self = Login.Login_page()
    
'''
# For Test
if __name__=="__main__":
  root = Customer_page('username','pass')
  root.mainloop()
  '''