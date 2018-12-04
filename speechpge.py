from tkinter import *
from tkinter import messagebox
import pymysql
import tkinter.ttk as ttk
import speech_recognition as sr

class speech:
    def __init__(self):
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
        

