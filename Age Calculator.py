from email.policy import default
from tkinter import *
from datetime import date
import datetime
age = Tk()
age.geometry("500x500")
age.title("AGE CALCULATOR")
n=StringVar()
day=IntVar()
month=IntVar()
year=IntVar()
L_name=Label(age,text="Name         ")
L_Day=Label(age,text="Day of Birth")
L_Month=Label(age,text="Month")
L_Year=Label(age,text="Year")
name=Entry(age,textvariable=n,width=10,font=("Helvetica",15))
Day=Entry(age,textvariable=day,width=2,font=("Helvetica",15))
Month=Entry(age,textvariable=month,width=2,font=("Helvetica",15))
Year=Entry(age,textvariable=year,width=4,font=("Helvetica",15))

def cal_age(owner,day,month,year):
    global L
    global mango
    x,y,z=day.get(),month.get(),year.get()
    user=owner.get()
    bd=date(int(z),int(y),int(x))
    no=datetime.datetime.now()
    now=date(int(no.year),int(no.month),int(no.day))
    a=now-bd
    mango=a.days
    L=Label(age,text=str(n.get())+' is now '+str(mango//365)+' years and '+str(mango%365)+' days',font=("Helvetica",15))
    L.grid(row=4,column=0,sticky='nsew')


L_name.grid(row=0,column=0,sticky='nsew')
name.grid(row=0,column=1,sticky='nsew')
L_Day.grid(row=2,column=0,sticky='nsew')
Day.grid(row=2,column=1,sticky='nsew')
L_Month.grid(row=2,column=2,sticky='nsew')
Month.grid(row=2,column=3,sticky='nsew')
L_Year.grid(row=2,column=4,sticky='nsew')
Year.grid(row=2,column=5,sticky='nsew')
submit=Button(age,text="Submit",padx=20,pady=20,command=lambda:cal_age(name,Day,Month,Year))
submit.grid(row=3,column=2,sticky='nsew')


Grid.rowconfigure(age,[0,1,2,3,4,5,6],weight=1)
Grid.columnconfigure(age,[0,1,2],weight=1)

L_name.config(font=("Cooper Black",10))
L_Day.config(font=("Cooper Black",10))
L_Month.config(font=("Cooper Black",10))
L_Year.config(font=("Cooper Black",10))

def resize(e):
    size=e.width / 10
    L_name.config(font=("Cooper Black",int(size)))
    L_Day.config(font=("Cooper Black",int(size)))
    L_Month.config(font=("Cooper Black",int(size)))
    L_Year.config(font=("Cooper Black",int(size)))


age.bind('<Configure>',resize)


age.mainloop()