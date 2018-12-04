from tkinter import *
from tkinter import messagebox
import pymysql
import tkinter.ttk as ttk
from viewpge import view123
from tkcalendar import Calendar,DateEntry 

class additm:
    def __init__(self):
        
        
        conn=pymysql.connect(host="localhost",user="root",password="python",db="grocery")
        a=conn.cursor()
        sql="select * from grocery"
        a.execute(sql)
        data=a.fetchall()
        """...................................."""
        self.window2=Tk()
        window2=self.window2
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
        e1.place(x=145,y=20)

        Label(window2, text='Item Name:',font=("Arial Bold",10)).place(x=10,y=60)
        e2=Entry(window2,textvariable=item)
        e2.insert(0,'')
        e2.bind("<FocusIn>", lambda args: e2.delete('0','end'))
        e2.place(x=145,y=60)

        Label(window2, text='Total Quantity:',font=("Arial Bold",10)).place(x=10,y=100)
        e3=Entry(window2,textvariable=quantity)
        e3.insert(0,'0')
        e3.bind("<FocusIn>", lambda args: e3.delete('0','end'))
        e3.place(x=145,y=100)

        Label(window2, text='Cost\Kg:',font=("Arial Bold",10)).place(x=10,y=140)
        e4=Entry(window2,textvariable=cost)
        e4.insert(0,'0.0')
        e4.bind("<FocusIn>", lambda args: e4.delete('0','end'))
        e4.place(x=145,y=140)

        def back1():
            window2.destroy()
            

        def back4():
            window2.destroy()
            viewob=view123()

        """Label(window2, text='Exp Date',font=("Arial Bold",10)).place(x=10,y=180)
        e5=Entry(window2,textvariable=expdate)
        
        
        #e5.bind("<FocusIn>", lambda args: e5.delete('0','end'))
        #expdate=DateEntry(window2,width=12,background='darkblue',foreground='white',borderwidth=2)
        expdate.place(x=135,y=180)
        e5.place(x=135,y=180)
        e5.insert(0,'YYYY-MM-DD')
        menu=Menu(window2)
        window2.config(menu=menu)
        submenu=Menu(menu)
        editmenu=Menu(menu)
        menu.add_cascade(label="Menu",menu=editmenu)
        editmenu.add_command(label="<--Back",command=back1)
        editmenu.add_command(label="   Exit",command=window2.destroy)"""

        Label(window2, text='ExpDate(dd-mm-yyy)',font=("Arial Bold",10)).place(x=10,y=180)
        e5=Entry(window2,textvariable=expdate)
        e5.place(x=145,y=180)
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
        Button(window2,text="View",fg="white",bd=5,bg="dark blue",font=("arial bold",10),command=back4).place(x=135,y=210)
        window2.mainloop()
