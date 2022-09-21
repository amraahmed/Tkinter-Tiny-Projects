from os import name
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os
class salesC:
    def __init__(self,root):
        self.root = root
        self.root.geometry("960x700+220+0")
        self.root.title("Inventory Management System")
        self.root.config(bg='white')
        self.root.focus_force()

#=====================================================================================================================================================
        self.invoicevar = StringVar()


#=====================================================================================================================================================
        title = Label(self.root,text='Customer Bills Details',justify=CENTER,font='arial 15 bold',bg='#4caf50',fg='white')
        title.place(x=100,y=100,width=800)

        invoicelbl = Label(self.root,text='Invoice No.',font='arial 15 bold',bg='white')
        invoicelbl.place(x=50,y=190)

        invoicent = Entry(self.root,textvariable=self.invoicevar,font='arial 10',bg='lightyellow')
        invoicent.place(x=200,y=190,width=180,height=28)

        srchbtn = Button(self.root,text='Search',font='arial 15 bold',bg='#2196f3',cursor='hand2')
        srchbtn.place(x=390,y=190,width=120,height=28)

        clrbtn = Button(self.root,text='Clear',font='arial 15 bold',fg='black',bg='lightgrey',cursor='hand2')
        clrbtn.place(x=520,y=190,width=120,height=28)

        salesF = Frame(self.root,bd=3,relief=RIDGE)
        salesF.place(x=50,y=230,width=200,height=330)

        scrolly = Scrollbar(salesF,orient=VERTICAL)

        
        self.salesList = Listbox(salesF,font='arial 15',bg='white',yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.salesList.yview)
        self.salesList.pack(fill=BOTH,expand=1)









#=====================================================================================================================================================
        billF = Frame(self.root,bd=3,relief=RIDGE)
        billF.place(x=280,y=230,width=410,height=330)

        biltitle = Label(billF,text='Customer Bills Area',justify=CENTER,font='arial 15 bold',bg='orange',)
        biltitle.pack(side=TOP,fill=X)


        
        scrolly1 = Scrollbar(billF,orient=VERTICAL)

        
        self.billList = Text(billF,font='arial 15',bg='white',yscrollcommand=scrolly1.set)
        scrolly1.pack(side=RIGHT,fill=Y)
        scrolly1.config(command=self.billList.yview)
        self.billList.pack(fill=BOTH,expand=1)



#=====================================================================================================================================================
        def show(self):
                self.saleslist.delete(1,END)
                print(os.listdir("bill"))
                 


#=====================================================================================================================================================
#=====================================================================================================================================================
#=====================================================================================================================================================
#=====================================================================================================================================================
#=====================================================================================================================================================
#=====================================================================================================================================================
#=====================================================================================================================================================
#=====================================================================================================================================================
#=====================================================================================================================================================
#=====================================================================================================================================================
#=====================================================================================================================================================
#=====================================================================================================================================================
#=====================================================================================================================================================


        

if __name__=="__main__":

    root=Tk()
    salesC(root)
    root.mainloop()