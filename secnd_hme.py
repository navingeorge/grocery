from tkinter import *
from tkinter import messagebox
import pymysql
import tkinter.ttk as ttk
from addpge import additm
from viewpge import view123
from delpge import delet
from speechpge import speech
import webbrowser


class home:
    def __init__(self):
        self.window1=Tk()
        window1=self.window1
        window1.title("Grocery Shop")
        canvas=Canvas(window1,width=450,height=250)
        window1.geometry("470x310")
        Label(window1,text="Flavour Town Grocery",font=("Arial Bold",18),fg="Dark Blue").place(x=80,y=5)
        def add_item():
            window1.destroy()
            addobj=additm()
            addobj=home()
        def view1():
            window1.destroy()
            viewobj=view123()
            viewobj=home()
        def clickdel():
            window1.destroy()
            delobj=delet()
            delobj=home()
        def voice():
            speechobj=speech()
            speechobj=home()
        def chatbot():
            webbrowser.open_new("https://bot.dialogflow.com/379b0f45-1d71-4619-a7c5-982da3918bfb")
    

        Button(window1,text="Add Item",fg="white",bd=5,bg="black",font=("arial bold",10),command=add_item).place(x=30,y=90)
        Button(window1,text="Delete Item",fg="white",bd=5,bg="black",font=("arial bold",10),command=clickdel).place(x=30,y=150)
        Button(window1,text="View Item",fg="white",bd=5,bg="black",font=("arial bold",10),command=view1).place(x=30,y=210)
        Button(window1,text="Speech",fg="White",bd=5,bg="Red",font=("Arial Bold",10),command=voice).place(x=380,y=150)
        Button(window1,text="ChatBot",fg="White",bd=5,bg="Green",font=("Arial Bold",10),command=chatbot).place(x=380,y=210)
        Button(window1,text="Logout",fg="Black",bd=5,font=("arial bold",10),command=window1.destroy).place(x=380,y=5)
       
        window1.mainloop()
    
