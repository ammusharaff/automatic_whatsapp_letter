# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 23:56:50 2022

@author:A Mohammed Musharaff
"""

from tkinter import *
from tkinter import messagebox
import pywhatkit as pwt
from datetime import datetime
import time

def body1():
    
    l1.destroy()
    b1.destroy()
    
    name_l = Label(win, text = 'Enter your Name', font=('calibre',10, 'bold'),background="gainsboro")
    Name = Entry(win, font=('calibre',10,'normal'))
    
    class_l = Label(win, text = 'Enter your class', font=('calibre',10, 'bold'),background="gainsboro")
    std = Entry(win,font=('calibre',10,'normal'))
    
    reason_l = Label(win, text = 'Enter one line reason', font=('calibre',10, 'bold'),background="gainsboro")
    reason = Entry(win, font=('calibre',10,'normal'))
    
    fdate_l=Label(win, text = 'Enter from date', font=('calibre',10, 'bold'),background="gainsboro")
    fdate = Entry(win, font=('calibre',10,'normal'))
    
    tdate_l=Label(win, text = 'Enter to date', font=('calibre',10, 'bold'),background="gainsboro")
    tdate = Entry(win, font=('calibre',10,'normal'))
    
    def body():
        b=("I am "+str(Name.get())+", a student of "+str(std.get())+". I want to bring to your kind attention that due to "+str(reason.get())+", I will be unable to come to college from "+str(fdate.get()+" to "+str(tdate.get()))+".\nI request you to provide me with leave for the dates mentioned above kindly. I assure you that I will catch up with my studies after coming back. I shall be grateful.\n\nThank you.\n\nYours faithfully,\n"+str(Name.get())) 
        name_l.destroy()
        Name.destroy()
        class_l.destroy()
        std.destroy()
        reason_l.destroy()
        fdate_l.destroy()
        reason.destroy()
        tdate_l.destroy()
        fdate.destroy()
        tdate.destroy()
        
        def hod():
            def new():
                messagebox.showinfo("showinfo", "wait for 1 more minute,your message will sent!",background="green")
                
            c1.destroy()
            c2.destroy()
            c3.destroy()
            c4.destroy()
            b2.destroy()
            new()
            t=datetime.now()
            h=int(t.strftime("%H"))
            n=t.strftime("%M")
            m=int(n)+2
            pwt.sendwhatmsg("+9194496229", b,h,m,wait_time=30)
            time.sleep(20)
            win.destroy()
            
        def ss():
            c1.destroy()
            c2.destroy()
            c3.destroy()
            c4.destroy()
            b2.destroy()
            t=datetime.now()
            h=int(t.strftime("%H"))
            n=t.strftime("%M")
            m=int(n)+1
            pwt.sendwhatmsg("+91888025", b,h,m,wait_time=30)
            time.sleep(20)
            win.destroy()
            
        def p1():
            c1.destroy()
            c2.destroy()
            c3.destroy()
            c4.destroy()
            b2.destroy()
            t=datetime.now()
            h=int(t.strftime("%H"))
            n=t.strftime("%M")
            m=int(n)+1
            pwt.sendwhatmsg("+918880", b,h,m,wait_time=30)
            time.sleep(20)
            exit()
            
        def p2():
            c1.destroy()
            c2.destroy()
            c3.destroy()
            c4.destroy()
            b2.destroy()
            t=datetime.now()
            h=int(t.strftime("%H"))
            n=t.strftime("%M")
            m=int(n)+1
            pwt.sendwhatmsg("+9190194", b,h,m,wait_time=30)
            time.sleep(20)
            win.destroy()
            
        def p3():
            c1.destroy()
            c2.destroy()
            c3.destroy()
            c4.destroy()
            b2.destroy()
            t=datetime.now()
            h=int(t.strftime("%H"))
            n=t.strftime("%M")
            m=int(n)+1
            pwt.sendwhatmsg("+9190194", b,h,m,wait_time=30)
            time.sleep(20)
            win.destroy()
            
        b2.destroy()
        c1=Button(win,text = "(HOD)",command=hod,height=5,width=50,background="sandy brown")
        c1.grid(row=0,column=1)
        c1.place(x=500,y=100)
        
        c2=Button(win,text = "Teacher 1 ",command=ss,height=5,width=50,background="sandy brown")
        c2.grid(row=1,column=1)
        c2.place(x=500,y=200)
        
        
        c3=Button(win,text = "proctor for rolno.(1-31)",command=p1,height=5,width=50,background="sandy brown")
        c3.grid(row=2,column=1)
        c3.place(x=500,y=300)
        
        c4=Button(win,text = "proctor for rolno.(31-62)",command=p2,height=5,width=50,background="sandy brown")
        c4.grid(row=3,column=1)
        c4.place(x=500,y=400)
       
        
    
        
        
    b2=Button(win,text="SUBMIT",command=body,font=20,height=1,width=10,background="sandy brown")
    
    
    name_l.grid(row=0,column=0)
    Name.grid(row=0,column=1)
    name_l.place(x=500,y=300)
    Name.place(x=650,y=300)
    
    class_l.grid(row=1,column=0)
    std.grid(row=1,column=1)
    class_l.place(x=500,y=330)
    std.place(x=650,y=330)
    
    
    reason_l.grid(row=2,column=0)
    reason.grid(row=2,column=1)
    reason_l.place(x=500,y=360)
    reason.place(x=650,y=360)
    
    fdate_l.grid(row=3,column=0)
    fdate.grid(row=3,column=1)
    fdate_l.place(x=500,y=390)
    fdate.place(x=650,y=390)
    
    tdate_l.grid(row=4,column=0)
    tdate.grid(row=4,column=1)
    tdate_l.place(x=500,y=420)
    tdate.place(x=650,y=420)
    
    b2.grid(row=5,column=0)
    b2.place(x=650,y=450)

    
    
win = Tk()## win is a top or parent window
win.geometry("700x700")
win.title("Whatsapp")
win.configure(background="gainsboro")

l1=Label(win,text="Write a Official Leave Letter",font=("TIMES_NEW_ROMAN",30,'bold'),height=1,width=30,background="gainsboro")
l1.pack()

b1=Button(win,text = "click here to start",command=body1,height=5,width=50,background="sandy brown")
b1.place(x=500,y=300)


win.mainloop()
