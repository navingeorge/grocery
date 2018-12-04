from tkinter import *
from tkinter import messagebox
import pymysql
import tkinter.ttk as ttk
import speech_recognition as sr  



    
window=Tk()
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

canvas=Canvas(window, width=1920, height=1080)
canvas.grid()
my_image = PhotoImage(file='C:\\Users\\Administrator\\Downloads\\0f605f13176acd87339a572a7a318d0e.png')
canvas.create_image(0, 0,anchor=NW, image=my_image)
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
        back()
    elif(username!=idname.get()):
        messagebox.showinfo("Error","Incorrect User Name")
    else:
        messagebox.showinfo("Error","Incorrect Password")

def back():
              
            window1=Tk()
            window1.title("Grocery Shop")
            canvas=Canvas(window1,width=450,height=250)
            window1.geometry("450x300")
            Label(window1,text="Flavour Town Grocery",font=("Arial Bold",18),fg="dark green").place(x=90,y=5)

            def view1():
                lf=Tk()
                lf.geometry("1320x330")
                lf.title("List Of Items")
                #lf.configure(background="black")
                comn=pymysql.connect(host="localhost",user="root",password="python",db="grocery")
                d=comn.cursor()
                sql="""SELECT * FROM grocery order by EXPDATE ASC"""
                d.execute(sql)
                rows=d.fetchall()
                #window1.destroy()

                def back3():
                    lf.destroy()
                    back()

                Button(lf,text="Back",fg="white",bd=4,bg="dark green",font=("arial bold",10),command=back3).place(x=50,y=5)
                #Button(lf,text="Delete",fg="white",bd=4,bg="dark blue",font=("arial bold",10),command=back3).place(x=1195,y=5)

                label_1=Label(lf,text="     Flavour Town Grocery List",font = "Arial 16 bold",fg="dark green").pack(anchor=N)

                tree = ttk.Treeview(lf, columns=("id","name","quantity","cost","exp"),height=10)
                vsb = ttk.Scrollbar(lf,orient="vertical")
                tree.configure(yscrollcommand=vsb.set)

                tree.column("id", anchor="c")
                tree.column("name", anchor="c") 
                tree.column("quantity", anchor="c") 
                tree.column("cost", anchor="c") 
                tree.column("exp", anchor="c")


                style=ttk.Style()
                style.configure("Treeview.Heading",font=(None,13,),)
                tree.tag_configure('oddrow',background='#ffffff')
                tree.tag_configure('evenrow',background='#B0C4DE')


                tree.heading("id", text="ID")
                tree.heading("name", text="NAME")
                tree.heading("quantity", text="QUANTITY")
                tree.heading("cost", text="COST")
                tree.heading("exp", text="EXP DATE")
                
                for i,item in enumerate(rows,1):
                    if(i%2==0):
                        tree.insert('','end',values=item,tags=('oddrow'))
                    else:
                        tree.insert('', 'end', values=item,tags=('evenrow'))
                 
         
                vsb.place(x=52,y=130)
                tree.place(x=50,y=40)

                comn.commit()
                comn.close()
                
            def view():
                lf=Tk()
                
                lf.geometry("1320x330")
                lf.title("List Of Items")
                #lf.configure(background="black")
                comn=pymysql.connect(host="localhost",user="root",password="python",db="grocery")
                d=comn.cursor()
                sql="""SELECT * FROM grocery order by EXPDATE ASC"""
                d.execute(sql)
                rows=d.fetchall()
                window1.destroy()

                def back3():
                    lf.destroy()
                    back()

                Button(lf,text="Back",fg="white",bd=4,bg="dark green",font=("arial bold",10),command=back3).place(x=50,y=5)
                #Button(lf,text="Delete",fg="white",bd=4,bg="dark blue",font=("arial bold",10),command=back3).place(x=1195,y=5)

                label_1=Label(lf,text="     Flavour Town Grocery List",font = "Arial 16 bold",fg="dark green").pack(anchor=N)

                tree = ttk.Treeview(lf, columns=("id","name","quantity","cost","exp"),height=10)
                vsb = ttk.Scrollbar(lf,orient="vertical")
                tree.configure(yscrollcommand=vsb.set)


                tree.column("id", anchor="c")
                tree.column("name", anchor="c") 
                tree.column("quantity", anchor="c") 
                tree.column("cost", anchor="c") 
                tree.column("exp", anchor="c")

                style=ttk.Style()
                style.configure("Treeview.Heading",font=(None,13,),)
                tree.tag_configure('oddrow',background='#ffffff')
                tree.tag_configure('evenrow',background='#B0C4DE')

                
          

                tree.heading("id", text="ID")
                tree.heading("name", text="NAME")
                tree.heading("quantity", text="QUANTITY")
                tree.heading("cost", text="COST")
                tree.heading("exp", text="EXP DATE")


                
                
                for i,item in enumerate(rows,1):
                    if(i%2==0):
                        tree.insert('','end',values=item,tags=('oddrow'))
                    else:
                        tree.insert('', 'end', values=item,tags=('evenrow'))
         
                vsb.place(x=1255,y=130)
                tree.place(x=50,y=40)

                comn.commit()
                comn.close()
                

            def add_item():
                window1.destroy()
                conn=pymysql.connect(host="localhost",user="root",password="python",db="grocery")
                a=conn.cursor()
                sql="select * from grocery"
                a.execute(sql)
                data=a.fetchall()
                """...................................."""
                window2=Tk()
                canvas=Canvas(window2,width=800,height=300)
                canvas.grid()
                window2.title("Add item")
                slno=IntVar()
                item=StringVar()
                quantity=IntVar()
                cost=DoubleVar()
                expdate=StringVar()

                Label(window2, text='Product_id:',font=("Arial Bold",10)).place(x=10,y=20)
                e1=Entry(window2,textvariable=slno)
                e1.insert(0,'0')
                e1.bind("<FocusIn>", lambda args: e1.delete('0','end'))
                e1.place(x=135,y=20)

                Label(window2, text='Item Name:',font=("Arial Bold",10)).place(x=10,y=60)
                e2=Entry(window2,textvariable=item)
                e2.insert(0,'')
                e2.bind("<FocusIn>", lambda args: e2.delete('0','end'))
                e2.place(x=135,y=60)

                Label(window2, text='Total Quantity:',font=("Arial Bold",10)).place(x=10,y=100)
                e3=Entry(window2,textvariable=quantity)
                e3.insert(0,'0')
                e3.bind("<FocusIn>", lambda args: e3.delete('0','end'))
                e3.place(x=135,y=100)

                Label(window2, text='Cost\Kg:',font=("Arial Bold",10)).place(x=10,y=140)
                e4=Entry(window2,textvariable=cost)
                e4.insert(0,'0.0')
                e4.bind("<FocusIn>", lambda args: e4.delete('0','end'))
                e4.place(x=135,y=140)

                def back1():
                    window2.destroy()
                    back()
                
                def back4():
                    window2.destroy()
                    view1()

                Label(window2, text='Exp Date',font=("Arial Bold",10)).place(x=10,y=180)
                e5=Entry(window2,textvariable=expdate)
                e5.place(x=135,y=180)
                menu=Menu(window2)
                window2.config(menu=menu)
                submenu=Menu(menu)
                editmenu=Menu(menu)
                menu.add_cascade(label="Menu",menu=editmenu)
                editmenu.add_command(label="<--Back",command=back1)
                editmenu.add_command(label="   Exit",command=window2.destroy)

                
                    

                def addto_database():
                    messagebox.showinfo("Success")
                    #window2.destroy()
                    conn=pymysql.connect(host="localhost",user="root",password="python",db="grocery")
                    a=conn.cursor()
                    sql="""INSERT INTO grocery(PRODUCT_ID,PRODUCT,QUANTITY,COST,EXPDATE)VALUES(%s,%s,%s,%s,%s)"""
                    a.execute(sql,(slno.get(),item.get(),quantity.get(),cost.get(),expdate.get()))
                    conn.commit()
                    conn.close()
                Button(window2,text="Update",fg="white",bd=5,bg="black",font=("arial bold",10),command=addto_database).place(x=210,y=210)
                #Button(window2,text="Update",fg="red",command=addto_database).place(x=210,y=210)
                Button(window2,text="View",fg="white",bd=5,bg="dark blue",font=("arial bold",10),command=back4).place(x=135,y=210)
                #Button(window2,text="View",fg="dark blue",command=back4).place(x=135,y=210)
                window2.mainloop()


                
            def clickdel():
                    
                
                    def list():
                        window1.destroy()
                        lst=Tk()
                        lst.geometry("1320x330")
                        lst.title("Delete Item")
                        con=pymysql.connect(host="localhost",user="root",password="python",db="grocery")
                        do=con.cursor()
                        sql="""SELECT * FROM grocery order by EXPDATE ASC"""
                        do.execute(sql)
                        rows=do.fetchall()

                        tree = ttk.Treeview(lst, columns=("id","name","quantity","cost","exp"),height=10)
                        vsb = ttk.Scrollbar(lst,orient="vertical")
                        tree.configure(yscrollcommand=vsb.set)


                        tree.column("id", anchor="c")
                        tree.column("name", anchor="c") 
                        tree.column("quantity", anchor="c") 
                        tree.column("cost", anchor="c") 
                        tree.column("exp", anchor="c")

                        style=ttk.Style()
                        style.configure("Treeview.Heading",font=(None,13,),)
                        tree.tag_configure('oddrow',background='#ffffff')
                        tree.tag_configure('evenrow',background='#B0C4DE')


                    
                        tree.heading("id", text="ID")
                        tree.heading("name", text="NAME")
                        tree.heading("quantity", text="QUANTITY")
                        tree.heading("cost", text="COST")
                        tree.heading("exp", text="EXP DATE")

                        for i,item in enumerate(rows,1):
                           if(i%2==0):
                             tree.insert('','end',values=item,tags=('oddrow'))
                           else:
                             tree.insert('', 'end', values=item,tags=('evenrow'))
                            

                       
                        vsb.place(x=52,y=130)
                        tree.place(x=50,y=40)

                        con.commit()
                        con.close()

       
                        def delete():

                           con=pymysql.connect(host="localhost",user="root",password="python",db="grocery")
                           do=con.cursor()
                           sql="""SELECT * FROM grocery"""
                           do.execute(sql)
                           rows=do.fetchall()

                           for i in tree.selection()[::-1]:
                               tree.delete(i)
                               print(i[1:])
                               j=IntVar()
                               j=int(i[1:])
                               j=j-1
                               print(j)
                               dat=rows[j]
                               print(dat[0])
                               sql=""" DELETE FROM grocery where PRODUCT=%s;"""
                               do.execute(sql,(dat[1]))
                               con.commit()
                               con.close()

                        def back3():
                           lst.destroy()
                           back()

                               
               
                        Button(lst,text="Delete",fg="white",bd=4,bg="dark blue",font=("arial bold",10),command=delete).place(x=1195,y=275)
                        Button(lst,text="Back",fg="white",bd=4,bg="dark green",font=("arial bold",10),command=back3).place(x=50,y=275)
                    list()
                    mainloop()

                            
            def remove_item():
                window1.destroy()
                window4=Tk()
                canvas=Canvas(window4,width=800,height=300)
                canvas.grid()
                window4.title("Remove item")
                rm=StringVar()
                Label(window4,text="Enter Product Name:").place(x=30,y=50)
                Entry(window4,textvariable=rm,width=25).place(x=150,y=50)
                def back2():
                    window4.destroy()
                    back()
                    
                def rm_itm():
                    
                    conn=pymysql.connect(host="localhost",user="root",password="python",db="grocery")
                    a=conn.cursor()

                    m="""SELECT * FROM grocery"""
                    a.execute(m)
                    c1=a.rowcount
                    
                    sql="""DELETE FROM grocery WHERE PRODUCT=%s"""
                    a.execute(sql,(rm.get()))

                    n="""SELECT * FROM grocery"""
                    a.execute(n)
                    c2=a.rowcount

                    if(c2<c1):
                        messagebox.showinfo("Success","Item Removed")
                    else:
                         messagebox.showinfo("Failed","Item Not Available")
                    
                    conn.commit()
                    conn.close()
                    
                    
                Button(window4,text="Remove",fg="white",bd=4,bg="dark blue",font=("arial bold",10),command=rm_itm).place(x=235,y=80)
                Button(window4,text="Back",fg="white",bd=4,bg="dark green",font=("arial bold",10),command=back2).place(x=150,y=80)
                window4.mainloop()

            def log_out():
                    messagebox.showinfo("success","Good Bye")
                    window1.destroy()
                    
                    
                    
            Button(window1,text="Add Item",fg="white",bd=5,bg="black",font=("arial bold",10),command=add_item).place(x=30,y=70)
            Button(window1,text="Delete Item",fg="white",bd=5,bg="black",font=("arial bold",10),command=clickdel).place(x=30,y=130)
            Button(window1,text="View Item",fg="white",bd=5,bg="black",font=("arial bold",10),command=view).place(x=30,y=190)
            Button(window1,text="Remove Item",fg="white",bd=5,bg="black",font=("arial bold",10),command=remove_item).place(x=30,y=250)
            Button(window1,text="Logout",fg="white",bd=5,bg="dark blue",font=("arial bold",10),command=log_out).place(x=350,y=70)
            #!/usr/bin/env python3                                                                                


            def audio():   
                # get audio from the microphone

                r = sr.Recognizer()                                                                                   
                with sr.Microphone() as source:                                                                       
                    print("Speak:")                                                                                   
                    audio = r.listen(source)   

                try:
                    nav=str(r.recognize_google(audio))
                    print("You said " + r.recognize_google(audio))
                    if nav=="add":
                        add_item()
                    elif nav=="delete":
                        clickdel()
                    elif nav=="view":
                        view()
                    else:
                        remove_item()
                        
                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results; {0}".format(e))

            Button(window1,text="Speech",fg="White",bd=5,bg="Red",font=("Arial Bold",10),command=audio).place(x=350,y=130)
    
            
                
                       
            window1.mainloop()
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


window.mainloop()






