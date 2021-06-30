# Hotel-Mangement-DBMS-Mini-Project

This is Hotel(Restaurant) management project that displays the menu of the hotel and takes orders from customers and generates bills which are recorded in database and also in file. We have considered requirements for the hotel side and have considered 3 major users i.e Customer, Chef, and Waiter.

<b>Frontend:</b> Python(tkinter)

<b>Database used:</b> Sqlite

<b>Scope of Mini Project:-</b>

Scope of project is for managing orders received from customers using 3 Actors/Users in process.

1: Customer side

Project Scope for Customers is only place order for parcels.


2: Hotel side

At the Hotel side there are two GUI's for handling orders i.e.Chef, Waiter GUI.

Chef:
Chef receives and completes orders.

Waiter:
Waiter can place orders for customers.



<b>Screen Shots:-</b>

Customer Login:
![Customer Login](https://github.com/JitendraJoshi2000/Hotel-Mangement-DBMS-Mini-Project/blob/main/Screenshots/customer%20login.png?raw=true)

Customer Signup:
![Customer Signup](https://github.com/JitendraJoshi2000/Hotel-Mangement-DBMS-Mini-Project/blob/main/Screenshots/customer%20signup.png?raw=true)

Customer Main Page:
![Customer Main Page](https://github.com/JitendraJoshi2000/Hotel-Mangement-DBMS-Mini-Project/blob/main/Screenshots/customer%20main%20page.png?raw=true)

Staff Login:
![Staff Login](https://github.com/JitendraJoshi2000/Hotel-Mangement-DBMS-Mini-Project/blob/main/Screenshots/staff%20login.png?raw=true)

Waiter:
![Waiter](https://github.com/JitendraJoshi2000/Hotel-Mangement-DBMS-Mini-Project/blob/main/Screenshots/waiter.png?raw=true)

Chef:
![Chef](https://github.com/JitendraJoshi2000/Hotel-Mangement-DBMS-Mini-Project/blob/main/Screenshots/chef.png?raw=true)

Generated Bill:
![Generated Bill](https://github.com/JitendraJoshi2000/Hotel-Mangement-DBMS-Mini-Project/blob/main/Screenshots/bill.png)


<b>Database Schema:-</b>

Customer( email_id varchar primary key , name varchar, phone_no integer, password varchar)
 
// For Customer

Orders( order_no varchar primary key , date varchar, time varchar, cust_id varchar references Customer(email_id ) )
 
Items( name varchar, rate integer, quantity integer, order_no varchar references Orders( order_no), status varchar, category varchar, primary key(name,order_no))
 
 
// For Waiter

waiter_order( order_no varchar primary key , table_no integer, date varchar, time varchar, cust_name varchar, cust_email varchar)
 
waiter_Items( name varchar, rate integer, quantity integer, order_no varchar references waiter_order( order_no), status varchar, category varchar,  primary key(name,order_no) )
 
 
// Record All Orders

Record_Order(order_no varchar primary key)
 
Record_Items( name varchar, rate integer, quantity integer, category varchar, order_no varchar references Record_Order(order_no))

ER Diagram:
![Generated Bill](https://github.com/JitendraJoshi2000/Hotel-Mangement-DBMS-Mini-Project/blob/main/Screenshots/ER%20Diagram.png)
