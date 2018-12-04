
from tkinter import *
from tkinter import messagebox
import pymysql
import tkinter.ttk as ttk
from secnd_hme import home


class main:
    def __init__(self,window):
        conn=pymysql.connect(host="localhost",user="root",password="python",db="grocery")
        a=conn.cursor()
        sql="select * from admin;"
        a.execute(sql)
        countrow=a.execute(sql)
        data=a.fetchall()
        temp=data[0]
        username=temp[0]
        password=temp[1]
        print(username,password)
        print("Welcome to Flavour Town Grocery Shop")

        idname=StringVar()
        pw=StringVar()

        
        window.title("Login")
        l=Label(window,text="   Flavour Town Grocery Shop",font=("Arial Bold",22),fg="Dark Blue").place(x=760,y=30)
        Label(window,text="Address:    Flavour Town Grocery Shop, Kazhakuttam, Trivandrum, Pin:695128",font=("Arial bold",12),fg="black").grid()
        Label(window,text='Username',font=("Arial Bold",10),fg="black").place(x=830,y=100) 
        Label(window,text='Password',font=("Arial Bold",10),fg="black").place(x=830,y=125)
        Entry(window,textvariable=idname).place(x=910, y=100)
        Entry(window,textvariable=pw,show="*").place(x=910, y=130)

        def login():
            if username==idname.get() and password==pw.get():
                window.destroy()
                obj=home()
            #nxt class name...........back()
            elif(username!=idname.get()):
                messagebox.showinfo("Error","Incorrect User Name")
       
         
            else:
                messagebox.showinfo("Error","Incorrect Password")

        Button(window,text="Submit",fg="red",font=("Arial Bold",10),command=login).place(x=910,y=170)

        def rst():
            window5=Tk()
            canvas =Canvas(window5,width=400,height=150)
            canvas.grid()
            window5.title("Reset Password")
            Label(window5, text='Enter Mobile Number:').place(x=10,y=20) 
            Label(window5, text='Enter Email Id:').place(x=10,y=60)
            Entry(window5).place(x=135,y=20)
            Entry(window5).place(x=135,y=60)
            
            def reset():
                messagebox.showinfo("Success")
                window5.destroy()
                print("A link to reset the password is send to the mobile number and email id")
            Button(window5,text="Submit",fg="red",command=reset).place(x=210,y=90)
            window5.mainloop()
                    
        def msg():
            print("enter your email-id or mobile number")
            messagebox.showinfo("Forgot Password")
        Button(window,text="Forgot Password",font=("Arial Bold",10),fg="black" ,command=rst).place(x=990,y=170)
root=Tk()
canvas=Canvas(root, width=1920, height=1080)
canvas.grid()
my_image = PhotoImage(file='C:\\Users\\Administrator\\Downloads\\0f605f13176acd87339a572a7a318d0e.png')
canvas.create_image(0, 0,anchor=NW, image=my_image)
obj=main(root)
root.mainloop()




                
