from tkinter import *
from datetime import date

root = Tk()
root.title("Countdown")
root.geometry("500x400")

panc = Label(root,text="Don't Panic",font="Helvetica 42",bg='black',fg='green')
panc.pack(pady=20,ipadx=10,ipady=10)
today = date.today()
ftod = today.strftime(f"%A - %B %d,%Y ")
todlbl = Label(root,text=f"Today is {ftod}")
todlbl.pack(pady=20)

year = 365
tod = int(today.strftime("%j"))
tody = int(today.strftime("%Y"))

left = year - tod
countdown = Label(root,text=f"There are only {left} days left in {tody}",font="Helvetica 20")
countdown.pack(pady=40)



root.mainloop()