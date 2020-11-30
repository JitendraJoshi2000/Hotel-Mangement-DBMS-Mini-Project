from tkinter import *
from tkinter import ttk
import Login
import sqlite3
import tkinter.messagebox as tmsg
import datetime
import os

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

    self.orderCategory = StringVar()
    combo_order = ttk.Combobox(order_category_frame,values=["Tabel","Parcel"],
                                textvariable=self.orderCategory)
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

    self.order_tabel = ttk.Treeview(order_tabel_frame,style = "Treeview",
                columns =("name","order_no"),
                yscrollcommand=scrollbar_order_y.set)

    self.order_tabel.heading("name",text="Order Name")
    self.order_tabel["show"] = "headings"
    self.order_tabel.column("name",anchor='center')
    self.order_tabel["displaycolumns"]=("name")

    scrollbar_order_y.pack(side=RIGHT,fill=Y)
    scrollbar_order_y.configure(command=self.order_tabel.yview)

    self.order_tabel.pack(fill=BOTH,expand=1)

    
    self.order_show_all() # To load tabel initially
    self.order_tabel.bind("<ButtonRelease-1>",self.load_item_from_order)

    ###########################################################################################
    
    
    #================Items Frame==============
    items_frame = Frame(self, bd=5, bg="lightgreen", relief=GROOVE, width=700)
    items_frame.pack(side=LEFT, fill="y")
    
    items_title_frame = Frame(items_frame,bg="lightgreen")
    items_title_frame.pack(side=TOP, fill="x", pady=5)

    show_all_button = ttk.Button(items_title_frame, text="Show All",
                            command=self.items_show_all)
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

    self.items_tabel = ttk.Treeview(items_tabel_frame,style = "Treeview",
                columns =("name","quantity","status","order_no"),xscrollcommand=scrollbar_items_x.set,
                yscrollcommand=scrollbar_items_y.set)

    self.items_tabel.heading("name",text="Name")
    self.items_tabel.heading("quantity",text="Quantity")
    self.items_tabel.heading("status",text="Status")
    self.items_tabel["displaycolumns"]=("name","quantity","status")
    self.items_tabel["show"] = "headings"
    self.items_tabel.column("name",width=300)
    self.items_tabel.column("quantity",width=100,anchor='center')

    scrollbar_items_x.pack(side=BOTTOM,fill=X)
    scrollbar_items_y.pack(side=RIGHT,fill=Y)

    scrollbar_items_x.configure(command=self.items_tabel.xview)
    scrollbar_items_y.configure(command=self.items_tabel.yview)

    self.items_tabel.pack(fill=BOTH,expand=1)

    self.items_show_all()
    self.items_tabel.bind("<ButtonRelease-1>",self.load_item_into_from_items)
    
    ###########################################################################################

    #================Item Frame==============
    item_frame = Frame(self, bd=5, bg="lightgreen", relief=GROOVE)
    item_frame.pack(fill="both",expand=True)

    selected_item_frame = Frame(item_frame, bg="lightgreen")
    selected_item_frame.pack(side=TOP,fill='x',pady=(100,10))

    selected_item_lable = Label(selected_item_frame, text="Item", 
                    font=("times new roman", 20, "bold"),bg = "lightgreen", fg="red")
    selected_item_lable.grid(row=0,column=0,padx=10)

    self.itemName = StringVar()
    self.itemName.set('')
    item_name = Entry(selected_item_frame, font="arial 12",textvariable=self.itemName,state=DISABLED, width=20)
    item_name.grid(row=0,column=1,padx=10)

    item_complete_button = ttk.Button(item_frame, text="Mark Completed",
                            command=self.item_complete_button_operation)
    item_complete_button.pack(padx=10,pady=10)

    selected_order_frame = Frame(item_frame, bg="lightgreen")
    selected_order_frame.pack(side=TOP,fill='x',pady=(100,10))

    selected_order_lable = Label(selected_order_frame, text="Order", 
                    font=("times new roman", 20, "bold"),bg = "lightgreen", fg="red")
    selected_order_lable.grid(row=0,column=0,padx=10)

    self.orderName = StringVar()
    self.orderName.set('')
    order_name = Entry(selected_order_frame, font="arial 12",textvariable=self.orderName,state=DISABLED, width=20)
    order_name.grid(row=0,column=1,padx=10)

    order_complete_button = ttk.Button(item_frame, text="Order Completed",
                            command=self.order_complete_button_operation)
    order_complete_button.pack(padx=10,pady=10)

#=========================Frontend Ends here

  def logout_operation(self):
    self.destroy()
    self = Login.Login_page()

  def order_show_operation(self):
    if self.orderCategory.get() not in ["Tabel","Parcel"]:
      tmsg.showinfo("Error", "Please select valid Choice")
      return
    if self.orderCategory.get()=="Tabel":
      self.order_tabel.delete(*self.order_tabel.get_children())
      db = sqlite3.connect('../hotel_database.db')
      cursor = db.cursor()
      cursor.execute("select table_no from waiter_order;")
      rows = cursor.fetchall()
      tabels = []
      for i in rows:
        tabels.append(i[0])
      tabels.sort()
      for tabel in tabels:
        self.order_tabel.insert('',END,values=[f"Tabel {tabel}"])
    elif self.orderCategory.get()=="Parcel":
      self.order_tabel.delete(*self.order_tabel.get_children())
      db = sqlite3.connect('../hotel_database.db')
      cursor = db.cursor()
      cursor.execute("select cust_id,order_no from Orders ORDER BY date,time;")
      rows = cursor.fetchall()
      for row in rows:
        self.order_tabel.insert('',END,values=[row[0],row[1]])

  def order_show_all(self):
    self.order_tabel.delete(*self.order_tabel.get_children())
    db = sqlite3.connect('../hotel_database.db')
    cursor = db.cursor()
    cursor.execute("select table_no from waiter_order;")
    rows = cursor.fetchall()
    tabels = []
    for i in rows:
      tabels.append(i[0])
    tabels.sort()
    for tabel in tabels:
      self.order_tabel.insert('',END,values=[f"Tabel {tabel}"])
    cursor2 = db.cursor()
    cursor2.execute("select cust_id,order_no from Orders ORDER BY date,time;")
    rows = cursor2.fetchall()
    for row in rows:
      self.order_tabel.insert('',END,values=[row[0],row[1]])

  def load_item_from_order(self,event):
    cursor_row = self.order_tabel.focus()
    contents = self.order_tabel.item(cursor_row)
    row = contents["values"]
    self.items_tabel.delete(*self.items_tabel.get_children())
    db = sqlite3.connect('../hotel_database.db')
    if (row[0].split(' ')[0]=='Tabel'):
      table_no = int(row[0].split(' ')[1])
      self.itemName.set('')
      self.orderName.set(f"Tabel {table_no}")
      cursor = db.cursor()
      cursor.execute(f"select order_no from waiter_order where table_no={table_no};")
      rows = cursor.fetchall()
      order_no = rows[0][0]
      cursor2 = db.cursor()
      cursor2.execute(f"select name,quantity,status,order_no from waiter_Items where order_no='{order_no}' AND status='Not Completed';")
      rows = cursor2.fetchall()
      for row in rows:
        self.items_tabel.insert('',END,values=[row[0],row[1],row[2],row[3]])
    else:
      order_no = row[1]
      self.itemName.set('')
      self.orderName.set(order_no)
      cursor = db.cursor()
      cursor.execute(f"select name,quantity,status,order_no from Items where order_no='{order_no}';")
      rows = cursor.fetchall()
      for row in rows:
        self.items_tabel.insert('',END,values=[row[0],row[1],row[2],row[3]])

  def items_show_all(self):
    self.items_tabel.delete(*self.items_tabel.get_children())
    db = sqlite3.connect('../hotel_database.db')
    cursor = db.cursor()
    cursor.execute(f"select name,quantity,status,waiter_Items.order_no from waiter_Items,waiter_order where waiter_order.order_no=waiter_Items.order_no AND status='Not Completed' order by waiter_order.table_no;")
    rows = cursor.fetchall()
    for row in rows:
       self.items_tabel.insert('',END,values=[row[0],row[1],row[2],row[3]])
    cursor2 = db.cursor()
    cursor2.execute(f"select name,quantity,status,order_no from Items;")
    rows = cursor2.fetchall()
    for row in rows:
       self.items_tabel.insert('',END,values=[row[0],row[1],row[2],row[3]])

  def load_item_into_from_items(self,event):
    cursor_row = self.items_tabel.focus()
    contents = self.items_tabel.item(cursor_row)
    row = contents["values"]
    self.itemName.set(row[0])
    order_no = str(row[3])
    if (order_no.count(';')==3):
      db = sqlite3.connect('../hotel_database.db')
      cursor = db.cursor()
      cursor.execute(f"select table_no from waiter_order where order_no='{order_no}'")
      rows = cursor.fetchall()
      self.orderName.set(f"Tabel {rows[0][0]}")
    else:
      self.orderName.set(row[3])

  def item_complete_button_operation(self):
    item_name = self.itemName.get()
    order_name = self.orderName.get()
    if item_name=='' or order_name=='':
      tmsg.showinfo("Error", "Please Select Item")
      return
    if (order_name.split(' ')[0]=='Tabel'):
      tabel_no = int(order_name.split(' ')[1])
      db = sqlite3.connect('../hotel_database.db')
      cursor = db.cursor()
      cursor.execute(f"select order_no from waiter_order where table_no={tabel_no}")
      rows = cursor.fetchall()
      order_no = rows[0][0]
      cursor2 = db.cursor()
      cursor2.execute(f"update waiter_Items SET status='Completed' where name='{item_name}' AND order_no='{order_no}'")
      db.commit()
    else:
      db = sqlite3.connect('../hotel_database.db')
      cursor = db.cursor()
      cursor.execute(f"update Items SET status='Completed' where name='{item_name}' AND order_no='{order_name}'")
      db.commit()
    self.itemName.set('')
    self.orderName.set('')
    self.load_item_from_order('event')

  def order_complete_button_operation(self):
    order_name = self.orderName.get()
    if order_name=='':
      tmsg.showinfo("Error", "Please Select Order")
      return
    if (order_name.split(' ')[0]=='Tabel'):
      tabel_no = int(order_name.split(' ')[1])
      db = sqlite3.connect('../hotel_database.db')
      cursor = db.cursor()
      cursor.execute(f"select order_no from waiter_order where table_no={tabel_no}")
      rows = cursor.fetchall()
      order_no = rows[0][0]
      cursor2 = db.cursor()
      cursor2.execute(f"update waiter_Items SET status='Completed' where order_no='{order_no}'")
      db.commit()
    else:
      order_no = self.orderName.get()
      x = datetime.datetime.now()
      db = sqlite3.connect('../hotel_database.db')
      #save order in Record_Order table
      cursor2 = db.cursor()
      cursor2.execute(f"insert into Record_Order values('{order_no}');")
      cursor = db.cursor()
      cursor3 = db.cursor()
      cursor4 = db.cursor()
      date = str(x.strftime("%d") + ',' + x.strftime("%m") + ',' + x.strftime("%Y"))
      time = str(x.strftime("%H") + ',' + x.strftime("%M") + ',' + x.strftime("%S"))
      #Contents of menu
      st = "\t\t\t\tMaharaja Hotel\n\t\t\tPimple Gurav, Pune-411061\n"
      st += "\t\t\tGST.NO:- 27AHXPP3379HIZH\n"
      st += "-"*61 + "BILL" + "-"*61 + "\nDate:- "
      st += str(x.strftime("%d") + '/' + x.strftime("%m") + '/' + x.strftime("%Y") +' '+ x.strftime("%a"))
      st += " "*10 + f"\t\t\t\t\t\tTime:- "
      st += str(x.strftime("%H") + ':' + x.strftime("%M") + ':' + x.strftime("%S"))
      st += f"\nCustomer Order No:- {order_no}\n"
      st += "-"*130 + "\n" + " "*4 + "DESCRIPTION\t\t\t\t\tRATE\tQUANTITY\t\tAMOUNT\n"
      st += "-"*130 + "\n"
      cursor.execute(f"select name, rate, quantity, category from Items where order_no='{order_no}';")
      rows = cursor.fetchall()
      total_price = 0
      for row in rows:
        name = row[0]
        rate = row[1]
        quantity = row[2]
        price = rate * quantity
        total_price += price
        category = row[3]
        cursor3.execute(f"insert into Record_Items values('{name}', {rate}, {quantity}, '{category}', '{order_no}');")
        cursor4.execute(f"delete from Items where order_no='{order_no}' AND name='{name}'")
        st += name + "\t\t\t\t\t" + str(rate) + "\t      " + str(quantity) + "\t\t  " + str(price) + "\n\n"
      st += "-"*130
      #Total Price
      st += f"\n\t\t\tTotal price : {total_price}\n"
      st += "-"*130
      #write into file
      folder = str(x.strftime("%d") + ',' + x.strftime("%m") + ',' + x.strftime("%Y"))
      if not os.path.exists(f"Bill Records\\{folder}"):
        os.makedirs(f"Bill Records\\{folder}")
      lis = order_no.split(';')
      file = open(f"Bill Records\\{folder}\\{lis[0]}_{date}_{time}.txt", "w")
      file.write(st)
      file.close()
      #delete order from database
      cursor5 = db.cursor()
      cursor5.execute(f"delete from Orders where order_no='{order_no}'")
      db.commit()
      self.items_tabel.delete(*self.items_tabel.get_children())
      self.order_show_all()

  def change_menu_button_operation(self):
    pass
    
    
    
    
'''   
# For Test
if __name__=="__main__":
  root = Chef_page()
  root.mainloop()
  '''