from tkinter import *
from tkinter import messagebox
import pymysql
import tkinter.ttk as ttk

import speech_recognition as sr  


class view123:
    def __init__(self):
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
            

        Button(lf,text="Back",fg="white",bd=4,bg="dark green",font=("arial bold",10),command=back3).place(x=50,y=5)
       

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
        style.configure("Treeview.Heading",font=(None,12,),)
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

