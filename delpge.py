from tkinter import *
from tkinter import messagebox
import pymysql
import tkinter.ttk as ttk



class delet:

    def __init__(self):



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
                    

                   

            Button(lst,text="Delete",fg="white",bd=4,bg="dark blue",font=("arial bold",10),command=delete).place(x=1195,y=275)
            Button(lst,text="Back",fg="white",bd=4,bg="dark green",font=("arial bold",10),command=back3).place(x=50,y=275)
               
            lst.mainloop()



