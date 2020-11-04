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
    
    change_menu_button = ttk.Button(title_frame, text="Change Menu",
                                  command=self.change_menu_button_operation)
    change_menu_button.pack(side=LEFT,padx=10)                          

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
    
    #================Order Frame==============
    order_frame = Frame(self, bd=5, bg="lightgreen", relief=GROOVE)
    order_frame.pack(side=LEFT, fill="y")
    
    order_label = Label(order_frame, text="Orders", 
                    font=("times new roman", 20, "bold"),bg = "lightgreen", fg="red", pady=0)
    order_label.pack(side=TOP,fill="x",pady=5)

    order_category_frame = Frame(order_frame,bg="lightgreen",pady=5)
    order_category_frame.pack(fill="x")

    orderCategory = StringVar()
    combo_order = ttk.Combobox(order_category_frame,values=["Tabel","Parcel"],
                                textvariable=orderCategory)
    combo_order.grid(row=0,column=0,padx=5,pady=5)

    show_button = ttk.Button(order_category_frame, text="Show",
                            command=self.order_show_operation)
    show_button.grid(row=0,column=1,padx=10,pady=5)

    show_all_button = ttk.Button(order_frame, text="Show All",
                                 command=self.order_show_all)
    show_all_button.pack(pady=(0,20))
    
    ############################# Order Tabel ##########################################
    order_tabel_frame = Frame(order_frame)
    order_tabel_frame.pack(fill=BOTH,expand=1)

    scrollbar_order_y = Scrollbar(order_tabel_frame,orient=VERTICAL)

    style = ttk.Style()
    style.configure("Treeview.Heading",font=("arial",13, "bold"))
    style.configure("Treeview",font=("arial",12),rowheight=25)

    order_tabel = ttk.Treeview(order_tabel_frame,style = "Treeview",
                columns =("name"),
                yscrollcommand=scrollbar_order_y.set)

    order_tabel.heading("name",text="Order Name")
    order_tabel["show"] = "headings"
    order_tabel.column("name",anchor='center')

    scrollbar_order_y.pack(side=RIGHT,fill=Y)
    scrollbar_order_y.configure(command=order_tabel.yview)

    order_tabel.pack(fill=BOTH,expand=1)

    order_tabel.insert('',END,values=["Tabel 1"])
    order_tabel.insert('',END,values=["Tabel 2"])
    order_tabel.insert('',END,values=["Order 101"])
    order_tabel.insert('',END,values=["Order 102"])
    #self.order_show_all() # To load tabel initially
    order_tabel.bind("<ButtonRelease-1>",self.load_item_from_order)

    ###########################################################################################
    
    
    #================Items Frame==============
    items_frame = Frame(self, bd=5, bg="lightgreen", relief=GROOVE, width=700)
    items_frame.pack(side=LEFT, fill="y")
    
    items_title_frame = Frame(items_frame,bg="lightgreen")
    items_title_frame.pack(side=TOP, fill="x", pady=5)

    show_all_button = ttk.Button(items_title_frame, text="Show All",
                            command=self.item_show_operation)
    show_all_button.pack(side='right',padx=10,pady=10)

    Items_label = Label(items_title_frame, text="Items", 
                    font=("times new roman", 20, "bold"),bg = "lightgreen", fg="red")
    Items_label.pack()

    ############################# items Tabel ##########################################
    items_tabel_frame = Frame(items_frame)
    items_tabel_frame.pack(fill=BOTH,expand=1)

    scrollbar_items_x = Scrollbar(items_tabel_frame,orient=HORIZONTAL)
    scrollbar_items_y = Scrollbar(items_tabel_frame,orient=VERTICAL)

    style = ttk.Style()
    style.configure("Treeview.Heading",font=("arial",13, "bold"))
    style.configure("Treeview",font=("arial",12),rowheight=25)

    items_tabel = ttk.Treeview(items_tabel_frame,style = "Treeview",
                columns =("name","quantity","status"),xscrollcommand=scrollbar_items_x.set,
                yscrollcommand=scrollbar_items_y.set)

    items_tabel.heading("name",text="Name")
    items_tabel.heading("quantity",text="Quantity")
    items_tabel.heading("status",text="Status")
    items_tabel["displaycolumns"]=("name","quantity","status")
    items_tabel["show"] = "headings"
    items_tabel.column("name",width=300)
    items_tabel.column("quantity",width=100,anchor='center')

    scrollbar_items_x.pack(side=BOTTOM,fill=X)
    scrollbar_items_y.pack(side=RIGHT,fill=Y)

    scrollbar_items_x.configure(command=items_tabel.xview)
    scrollbar_items_y.configure(command=items_tabel.yview)

    items_tabel.pack(fill=BOTH,expand=1)


    items_tabel.insert('',END,values=["Masala Dosa",2,"Not Completed"])
    items_tabel.insert('',END,values=["Tea",1,"Completed"])
    items_tabel.insert('',END,values=["Coffee",3,"Not Completed"])
    items_tabel.insert('',END,values=["Roti",1,"Completed"])
    items_tabel.insert('',END,values=["Sandwitch",2,"Completed"])

    self.items_show_all()
    items_tabel.bind("<ButtonRelease-1>",self.load_item_into_from_items)
    
    ###########################################################################################

    #================Item Frame==============
    item_frame = Frame(self, bd=5, bg="lightgreen", relief=GROOVE)
    item_frame.pack(fill="both",expand=True)

    selected_item_frame = Frame(item_frame, bg="lightgreen")
    selected_item_frame.pack(side=TOP,fill='x',pady=(100,10))

    selected_item_lable = Label(selected_item_frame, text="Item", 
                    font=("times new roman", 20, "bold"),bg = "lightgreen", fg="red")
    selected_item_lable.grid(row=0,column=0,padx=10)

    itemName = StringVar()
    itemName.set("Masala Dosa")
    item_name = Entry(selected_item_frame, font="arial 12",textvariable=itemName,state=DISABLED, width=20)
    item_name.grid(row=0,column=1,padx=10)

    item_complete_button = ttk.Button(item_frame, text="Mark Completed",
                            command=self.item_complete_button_operation)
    item_complete_button.pack(padx=10,pady=10)

    selected_order_frame = Frame(item_frame, bg="lightgreen")
    selected_order_frame.pack(side=TOP,fill='x',pady=(100,10))

    selected_order_lable = Label(selected_order_frame, text="Order", 
                    font=("times new roman", 20, "bold"),bg = "lightgreen", fg="red")
    selected_order_lable.grid(row=0,column=0,padx=10)

    orderName = StringVar()
    orderName.set("Table 1")
    order_name = Entry(selected_order_frame, font="arial 12",textvariable=orderName,state=DISABLED, width=20)
    order_name.grid(row=0,column=1,padx=10)

    order_complete_button = ttk.Button(item_frame, text="Order Completed",
                            command=self.order_complete_button_operation)
    order_complete_button.pack(padx=10,pady=10)
    
  def logout_operation(self):
    self.destroy()
    self = Login.Login_page()

  def order_show_operation(self):
    pass

  def order_show_all(self):
    pass

  def load_item_from_order(self,e):
    pass

  def item_show_operation(self):
    pass

  def items_show_all(self):
    pass

  def load_item_into_from_items(self,e):
    pass

  def item_complete_button_operation(self):
    pass

  def order_complete_button_operation(self):
    pass

  def change_menu_button_operation(self):
    pass
    
    
    
    
    
# For Test
if __name__=="__main__":
  root = Chef_page()
  root.mainloop()