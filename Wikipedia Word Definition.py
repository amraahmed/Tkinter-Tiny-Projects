from datetime import date
from tkinter import *
import wikipedia as wiki

root = Tk()
root.title("Wiki")
root.geometry("700x675")


def clear():
    srchent.delete(0,END)
    mytxt.delete(0.0,END)

def search():
    data=wiki.summary(srchent.get())

    clear()

    mytxt.insert(0.0,data)


    



lblf = LabelFrame(root,text="Search Box")
lblf.pack(pady=20)


srchent = Entry(lblf,font='Arial 16',width=37)
srchent.pack(pady=20,padx=20)

showF = Frame(root,)
showF.pack(pady=5)

scrolly = Scrollbar(showF)
scrolly.pack(side=RIGHT,fill=Y)


scrollx = Scrollbar(showF,orient=HORIZONTAL)
scrollx.pack(side=BOTTOM,fill=X)

mytxt = Text(showF,yscrollcommand=scrolly.set,wrap='none',xscrollcommand=scrollx.set)
mytxt.pack()
scrolly.config(command=mytxt.yview)
scrollx.config(command=mytxt.xview)

btnF= Frame(root)
btnF.pack(pady=10)

srchbtn = Button(btnF,text="Search",font='Helvatica 34',fg="#3a3a3a",command=search)
srchbtn.grid(row=0,column=0,padx=20)
 
clearbtn = Button(btnF,text="Clear",font='Helvatica 34',fg="#3a3a3a",command=clear)
clearbtn.grid(row=0,column=1)
 



root.mainloop()