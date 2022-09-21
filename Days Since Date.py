from tkinter import *
from datetime import date

root = Tk()
root.title("Countdown")
root.geometry("500x400")

panc = Label(root,text="Days Since",font="Helvetica 42",fg='Black')
panc.pack(pady=20,ipadx=10,ipady=10)


days = IntVar()
mnths = IntVar()
ys = IntVar()

def submitcmd():
    dc = day1.get()
    mc = mnth1.get()
    yc = yer.get()
    dc = int(day1.get()) 
    mc = int(mnth1.get())
    yc =int(yer.get())
        
    today = date.today()
    ftod = today.strftime(f"%A - %B %d,%Y ")
    todlbl = Label(root,text=f"Today is {ftod}")
    todlbl.pack(pady=30)

    todaytod = int(today.strftime(f"%d"))
    yeartod = int(today.strftime("%Y"))
    monthtod = int(today.strftime("%m"))


    daydiff = dc - todaytod
    monthdiff = mc - monthtod
    yeardiff = yc - yeartod
    totdiff = (daydiff+(monthdiff*30)+(yeardiff*365)) 

    countdown.config(text="It has been {} days since {} {} {}".format(abs(totdiff),day1.get(),mnth1.get(),yer.get()),font="Helvetica 20")
    
    




day1 = Entry(root,font="Helvetica 26",textvariable=days)
day1.place(x=100,y=110,width=80,height=50)
mnth1= Entry(root,font="Helvetica 26",textvariable=mnths)
mnth1.place(x=170,y=110,width=80,height=50)
yer= Entry(root,font="Helvetica 26",textvariable=ys)
yer.place(x=250,y=110,width=100,height=50)




countdown = Label(root,text="",font="Helvetica 20")
countdown.pack(pady=40)




submit = Button(root,text='submit',command=submitcmd)
submit.pack()
root.mainloop()