from os import name
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class supplierC:
    def __init__(self,root):
        self.root = root
        self.root.geometry("960x700+220+0")
        self.root.title("Inventory Management System")
        self.root.config(bg='white')
        self.root.focus_force()

        #======================================================================

        self.invoiceVar = StringVar()
        self.nameVar = StringVar()
        self.contactVar = StringVar()
        self.descVar = StringVar()
        self.searchbyVar = StringVar() 
        self.searchVar = StringVar()      


        
        #======================================================================

        serchF = LabelFrame(self.root,text="Search supplier",bg='white',font='arial 10 bold',bd=2,relief=RIDGE)
        serchF.place(x=200,y=20,width=600,height=70)

        cbserch = ttk.Combobox(serchF,textvariable=self.searchbyVar,values=("Select","ID","Name","Phone Number"),state='readonly',justify=CENTER)
        cbserch.place(x=10,y=10,width=180)
        cbserch.current(0)

        txtsrch = Entry(serchF,textvariable=self.searchVar,font='arial 15',bg='lightyellow')
        txtsrch.place(x=200,y=10)

        srchbtn = Button(serchF,text='Search',command=self.srch,font='arial 15',bg='#4caf50',fg='white')
        srchbtn.place(x=410,y=10,width=150,height=30)
        #=========================================================================

        title = Label(self.root,text='Supplier Details',justify=CENTER,font='arial 15 bold',bg='#4caf50',fg='white')
        title.place(x=100,y=100,width=800)
        #===========================================================================================
        supplierinv = Label(self.root,text='Suplier ID',font='arial 15 bold',bg='white')
        supplierinv.place(x=30,y=150)

        suppname = Label(self.root,text='Name',font='arial 15 bold',bg='white')
        suppname.place(x=30,y=200)

        
        suppcontact = Label(self.root,text='Contact',font='arial 15 bold',bg='white')
        suppcontact.place(x=30,y=250,)

        
        suppdes = Label(self.root,text='Description',font='arial 15 bold',bg='white')
        suppdes.place(x=30,y=300,)


        invoiceEnt = Entry(self.root,textvariable=self.invoiceVar,bg="white")
        invoiceEnt.place(x=180,y=150,width=180,height=25)

        nameEnt = Entry(self.root,textvariable=self.nameVar,bg="white")
        nameEnt.place(x=180,y=200,width=180,height=25)

        contactEnt = Entry(self.root,textvariable=self.contactVar,bg="white")
        contactEnt.place(x=180,y=250,width=180,height=25)

        descEnt = Entry(self.root,textvariable=self.descVar,bg="white")
        descEnt.place(x=180,y=300,width=180,height=50)

        #==============================================================================

        addbtn = Button(self.root,text='Add',font='arial 15',bg='#4caf50',fg='white',command=self.add)
        addbtn.place(x=460,y=365,width=110,height=30)

        updatebtn = Button(self.root,text='Update',font='arial 15',bg='#4caf50',fg='white',command=self.update)
        updatebtn.place(x=580,y=365,width=110,height=30)

        clearbtn = Button(self.root,command=self.clear,text='Clear',font='arial 15',bg='#4caf50',fg='white')
        clearbtn.place(x=700,y=365,width=110,height=30)

        deletebtn = Button(self.root,text='Delete',font='arial 15',command=self.delete,bg='#4caf50',fg='white')
        deletebtn.place(x=820,y=365,width=110,height=30)

        #========================================================================================
        empF = Frame(self.root,bd=3,relief=RIDGE)
        empF.place(x=0,y=400,relwidth=1,height=300)

        scrolly = Scrollbar(empF,orient=VERTICAL)
        scrollx = Scrollbar(empF,orient=HORIZONTAL)
        
        self.suppliertable = ttk.Treeview(empF,columns=("invoice","Name",'contact','desc',),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(fill=X,side=BOTTOM)
        scrolly.pack(fill=Y,side=LEFT)

        scrollx.config(command=self.suppliertable.xview)
        scrolly.config(command=self.suppliertable.yview)

        self.suppliertable.pack(fill=BOTH,expand=1)

        self.suppliertable.heading("invoice",text='invoice')
        self.suppliertable.heading("Name",text='Name')
        self.suppliertable.heading("contact",text='contact')
        self.suppliertable.heading("desc",text='desc')
        


        self.suppliertable.column("invoice",width=100)
        self.suppliertable.column("Name",width=400)        
        self.suppliertable.column("contact",width=120)
        self.suppliertable.column("desc",width=30)
        self.suppliertable.bind("<ButtonRelease-1>",self.getData)

        self.suppliertable["show"]='headings'
        self.show()





    def add(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.invoiceVar.get() == "":
                messagebox.showerror("Error","Supplier must have an ID",parent=self.root)

            else:
                cur.execute("Select * from supplier where invoice =?",(self.invoiceVar.get()))
                row = cur.fetchone()

                if row !=None:
                    messagebox.showerror("Error","This ID is already assigned")
                else:
                    cur.execute("Insert into supplier (invoice, name, contact,desc) values(?,?,?,?)",(
                        self.invoiceVar.get(),
                        self.nameVar.get(),
                        self.contactVar.get(),
                        self.descVar.get(),                       
                    ))

                    con.commit()
                    messagebox.showinfo("Sucess","supplier added sucessfuly",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)

            



    def show(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM supplier")
            rows = cur.fetchall()
            self.suppliertable.delete(*self.suppliertable.get_children())
            for row in rows:
                self.suppliertable.insert('',END, values=row)
        

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)


    def update(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.invoiceVar.get() == "":
                messagebox.showerror("Error","supplier must have an ID",parent=self.root)

            else:
                cur.execute("Select * from supplier where invoice =?",(self.invoiceVar.get(),))
                row = cur.fetchone()

                if row ==None:
                    messagebox.showerror("Error","Invalid ID")
                else:
                    cur.execute("Update supplier set Name=?, Phone=?, Email=?, Gender=?, Department=?, Adress=?, Salary=? where id=?",(
                        self.nameVar.get(),
                        self.phoneVar.get(),
                        self.emailvar.get(),
                        self.genderVar.get(),
                        self.departmentVar.get(),
                        self.adressVar.get(),
                        self.salaryVar.get(),
                        self.invoiceVar.get(),
                    ))

                    con.commit()
                    messagebox.showinfo("Sucess","supplier data has been updated sucessfuly",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)
            

    def getData(self,ev):
        f= self.suppliertable.focus()
        content = (self.suppliertable.item(f))
        row = content['values']
        print(row)
        self.invoiceVar.set(row[0]),
        self.nameVar.set(row[1]),
        self.contactVar.set(row[2])
        self.descVar .set(row[3]),
        

    def delete(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.invoiceVar.get()=="":
                messagebox.showerror("Error","Please Enter an ID")
            else:
                cur.execute("Select * from supplier where invoice=?",(self.invoiceVar.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Error")
                else:
                    delmsg = messagebox.askyesno("Confirm","Do you want to delete {} from your database".format(self.nameVar.get()))
                    if delmsg == True:
                        cur.execute("DELETE FROM supplier where invoice=?",(self.invoiceVar.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","supplier has been deleted",parent=self.root)
                        self.show
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",)
        self.show()

    def clear(self):
        self.invoiceVar.set(""),
        self.nameVar.set(""),
        self.contactVar.set(""),
        self.descVar.set(""),        
        self.searchVar.set(""),
        self.searchbyVar.set("Select"),
        self.show()


    def srch(self):
            con = sqlite3.connect(database="ims.db")
            cur = con.cursor()
            try:
                if self.searchbyVar.get() == "Select":
                    messagebox.showerror("Error","Enter the search type")
                elif self.searchVar.get() == "":
                    messagebox.showerror("Error","search input is required",parent=self.root)
                else:
                    cur.execute("select * from supplier where "+self.searchbyVar.get()+" LIKE '%"+self.searchVar.get()+"%'")

                    rows = cur.fetchall()
                    if len(rows) != 0:
                        self.suppliertable.delete(*self.suppliertable.get_children())
                        for row in rows:
                            self.suppliertable.insert('',END,values=row)                    
                    else:
                        messagebox.showerror("Error","No record found",parent=self.root)
                con.commit()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{str(ex)}",)
            













        

if __name__=="__main__":

    root=Tk()
    supplierC(root)
    root.mainloop()