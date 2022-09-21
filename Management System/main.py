from tkinter import *
from employee import employeeC
from sup import supplierC

class IMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg='white')
        



        #///////////////////////////////////////////////////////////////////////////////////////////

        title = Label(self.root,text='Inventory Mangement System',fg='white',bg='#010c48',font='arial 40 bold',anchor='w',padx=20)
        title.place(x=0,y=0,relwidth=1,height=70)

        #///////////////////////////////////////////////////////////////////////////////////////////
        logout = Button(self.root,text='Logout',bg='yellow',font='arial 15 bold',cursor="hand2")
        logout.place(x=1050,y=10,height=30,width=150) 
        #///////////////////////////////////////////////////////////////////////////////////////////

        self.clock = Label(self.root,text='Welcome to Inventory Management System\t\t Date: DD-MM-YY\t\t Time:HH:MM ',font='arial 15 bold',bg='#4d636d',fg='white')
        self.clock.place(x=0,y=70,relwidth=1,height=30)

        #///////////////////////////////////////////////////////////////////////////////////////////

        lftMenu = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        lftMenu.place(x=0,y=102,width=200,height=600)

        menulbl = Label(lftMenu,text="Menu",font='arial 20 bold',bg='#009688')
        menulbl.pack(side=TOP,fill=X)

        employee = Button(lftMenu,text='Employee',command=self.employee,compound=LEFT,padx=40,anchor="w",bg='white',cursor='hand2',bd=3,font='arial 15 bold')
        employee.pack(side=TOP,fill=X)

        supp = Button(lftMenu,text='Supplier',command=self.supplier,compound=LEFT,padx=40,anchor="w",bg='white',cursor='hand2',bd=3,font='arial 15 bold')
        supp.pack(side=TOP,fill=X)

        catg = Button(lftMenu,text='Category',compound=LEFT,padx=40,anchor="w",bg='white',cursor='hand2',bd=3,font='arial 15 bold')
        catg.pack(side=TOP,fill=X)

        prod = Button(lftMenu,text='Products',compound=LEFT,padx=40,anchor="w",bg='white',cursor='hand2',bd=3,font='arial 15 bold')
        prod.pack(side=TOP,fill=X)

        sale = Button(lftMenu,text='Sales',compound=LEFT,padx=40,anchor="w",bg='white',cursor='hand2',bd=3,font='arial 15 bold')
        sale.pack(side=TOP,fill=X)

        ext = Button(lftMenu,text='Exit',compound=LEFT,padx=40,anchor="w",bg='white',cursor='hand2',bd=3,font='arial 15 bold')
        ext.pack(side=TOP,fill=X) 
        #///////////////////////////////////////////////////////////////////////////////////////////

        self.emplbl = Label(self.root,text='Total Employees [ ]',bd=5,bg='#33bbf9',fg='white',font='arial 20 bold',relief=RIDGE)
        self.emplbl.place(x=250,y=120,height=150,width=300)

        self.suplbl = Label(self.root,text='Total Suppliers [ ]',bd=5,bg='#33bbf9',fg='white',font='arial 20 bold',relief=RIDGE)
        self.suplbl.place(x=600,y=120,height=150,width=300)

        self.catlbl = Label(self.root,text='Total Categories [ ]',bd=5,bg='#33bbf9',fg='white',font='arial 20 bold',relief=RIDGE)
        self.catlbl.place(x=950,y=120,height=150,width=300)

        self.prodlbl = Label(self.root,text='Total Products [ ]',bd=5,bg='#33bbf9',fg='white',font='arial 20 bold',relief=RIDGE)
        self.prodlbl.place(x=250,y=300,height=150,width=300)

        self.salslbl = Label(self.root,text='Total Sales [ ]',bd=5,bg='#33bbf9',fg='white',font='arial 20 bold',relief=RIDGE)
        self.salslbl.place(x=600,y=300,height=150,width=300)


        #///////////////////////////////////////////////////////////////////////////////////////////

    def employee(self):
        self.newWin = Toplevel(self.root)
        self.newObj = employeeC(self.newWin)


    def supplier(self):
        self.newWin = Toplevel(self.root)
        self.newObj = supplierC(self.newWin)




        #///////////////////////////////////////////////////////////////////////////////////////////








if __name__=="__main__":

    root=Tk()
    IMS(root)
    root.mainloop()
