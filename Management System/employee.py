from os import name
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class employeeC:
    def __init__(self,root):
        self.root = root
        self.root.geometry("960x700+220+0")
        self.root.title("Inventory Management System")
        self.root.config(bg='white')
        self.root.focus_force()

        #======================================================================

        self.idVar = StringVar()
        self.nameVar = StringVar()
        self.phoneVar = StringVar()
        self.emailvar = StringVar()
        self.adressVar = StringVar()
        self.genderVar = StringVar()
        self.departmentVar = StringVar()
        self.salaryVar = StringVar() 
        self.searchbyVar = StringVar() 
        self.searchVar = StringVar()      

        #======================================================================

        serchF = LabelFrame(self.root,text="Search Employee",bg='white',font='arial 10 bold',bd=2,relief=RIDGE)
        serchF.place(x=200,y=20,width=600,height=70)

        cbserch = ttk.Combobox(serchF,textvariable=self.searchbyVar,values=("Select","ID","Name","Phone Number"),state='readonly',justify=CENTER)
        cbserch.place(x=10,y=10,width=180)
        cbserch.current(0)

        txtsrch = Entry(serchF,textvariable=self.searchVar,font='arial 15',bg='lightyellow')
        txtsrch.place(x=200,y=10)

        srchbtn = Button(serchF,text='Search',command=self.srch,font='arial 15',bg='#4caf50',fg='white')
        srchbtn.place(x=410,y=10,width=150,height=30)
        #=========================================================================

        title = Label(self.root,text='Employee Details',justify=CENTER,font='arial 15 bold',bg='#4caf50',fg='white')
        title.place(x=100,y=100,width=800)
        #===========================================================================================
        employeeid = Label(self.root,text='ID',font='arial 15 bold',bg='white')
        employeeid.place(x=30,y=150)

        employeename = Label(self.root,text='Name',font='arial 15 bold',bg='white')
        employeename.place(x=30,y=200)

        employeephone = Label(self.root,text='phone',font='arial 15 bold',bg='white')
        employeephone.place(x=30,y=250)

        employeeemail = Label(self.root,text='E-mail',font='arial 15 bold',bg='white')
        employeeemail.place(x=30,y=300,)

        employeegender = Label(self.root,text='Gender',font='arial 15 bold',bg='white')
        employeegender.place(x=30,y=350)

        employeedep = Label(self.root,text='Department',font='arial 15 bold',bg='white')
        employeedep.place(x=580,y=150)

        employeeadrss = Label(self.root,text='Adress',font='arial 15 bold',bg='white')
        employeeadrss.place(x=580,y=200)

        employeesalary = Label(self.root,text='Salary',font='arial 15 bold',bg='white')
        employeesalary.place(x=580,y=320,)


        idEnt = Entry(self.root,textvariable=self.idVar,bg="white")
        idEnt.place(x=180,y=150,width=180,height=25)

        nameEnt = Entry(self.root,textvariable=self.nameVar,bg="white")
        nameEnt.place(x=180,y=200,width=180,height=25)

        phoneEnt = Entry(self.root,textvariable=self.phoneVar,bg="white")
        phoneEnt.place(x=180,y=250,width=180,height=25)

        emailEnt = Entry(self.root,textvariable=self.emailvar,bg="white")
        emailEnt.place(x=180,y=300,width=180,height=25)

        genEnt = ttk.Combobox(self.root,textvariable=self.genderVar,values=("Male","Female"),state='readonly',justify=CENTER)
        genEnt.place(x=180,y=350,width=180,height=25)

        DepEnt = Entry(self.root,textvariable=self.departmentVar,bg="white")
        DepEnt.place(x=730,y=150,width=180,height=25)

        adrssEnt = Entry(self.root,textvariable=self.adressVar,bg="white")
        adrssEnt.place(x=730,y=200,width=180,height=100)

        SalaryEnt = Entry(self.root,textvariable=self.salaryVar,bg="white")
        SalaryEnt.place(x=730,y=320,width=180,height=25)


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
        
        self.employeeTable = ttk.Treeview(empF,columns=("ID","Name",'Phone','Email','Gender','Department','Adress','Salary'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(fill=X,side=BOTTOM)
        scrolly.pack(fill=Y,side=LEFT)

        scrollx.config(command=self.employeeTable.xview)
        scrolly.config(command=self.employeeTable.yview)

        self.employeeTable.pack(fill=BOTH,expand=1)

        self.employeeTable.heading("ID",text='ID')
        self.employeeTable.heading("Name",text='Name')
        self.employeeTable.heading("Phone",text='Phone')
        self.employeeTable.heading("Email",text='Email')
        self.employeeTable.heading("Gender",text='Gender')
        self.employeeTable.heading("Department",text='Department')
        self.employeeTable.heading("Adress",text='Adress')
        self.employeeTable.heading("Salary",text='Salary')
        self.employeeTable["show"]='headings'



        self.employeeTable.column("ID",width=160)
        self.employeeTable.column("Name",width=400)
        self.employeeTable.column("Phone",width=100)
        self.employeeTable.column("Email",width=120)
        self.employeeTable.column("Gender",width=30)
        self.employeeTable.column("Department",width=90)
        self.employeeTable.column("Adress",width=120)
        self.employeeTable.column("Salary",width=180)
        self.employeeTable.bind("<ButtonRelease-1>",self.getData)


        self.show()





    def add(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.idVar.get() == "":
                messagebox.showerror("Error","Employee must have an ID",parent=self.root)

            else:
                cur.execute("Select * from employee where id =?",(self.idVar.get(),))
                row = cur.fetchone()

                if row !=None:
                    messagebox.showerror("Error","This ID is already assigned")
                else:
                    cur.execute("Insert into employee(id, Name, Phone, Email, Gender, Department, Adress, Salary) values(?,?,?,?,?,?,?,?)",(
                        self.idVar.get(),
                        self.nameVar.get(),
                        self.phoneVar.get(),
                        self.emailvar.get(),
                        self.genderVar.get(),
                        self.departmentVar.get(),
                        self.adressVar.get(),
                        self.salaryVar.get(),
                    ))

                    con.commit()
                    messagebox.showinfo("Sucess","Employee added sucessfuly",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)

            



    def show(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM employee")
            rows = cur.fetchall()
            self.employeeTable.delete(*self.employeeTable.get_children())
            for row in rows:
                self.employeeTable.insert('',END, values=row)
        

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)


    def update(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.idVar.get() == "":
                messagebox.showerror("Error","Employee must have an ID",parent=self.root)

            else:
                cur.execute("Select * from employee where id =?",(self.idVar.get(),))
                row = cur.fetchone()

                if row ==None:
                    messagebox.showerror("Error","Invalid ID")
                else:
                    cur.execute("Update employee set Name=?, Phone=?, Email=?, Gender=?, Department=?, Adress=?, Salary=? where id=?",(
                        self.nameVar.get(),
                        self.phoneVar.get(),
                        self.emailvar.get(),
                        self.genderVar.get(),
                        self.departmentVar.get(),
                        self.adressVar.get(),
                        self.salaryVar.get(),
                        self.idVar.get(),
                    ))

                    con.commit()
                    messagebox.showinfo("Sucess","Employee data has been updated sucessfuly",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)
            

    def getData(self,ev):
        f= self.employeeTable.focus()
        content = (self.employeeTable.item(f))
        row = content['values']
        print(row)
        self.idVar.set(row[0]),
        self.nameVar.set(row[1]),
        self.phoneVar.set(row[2]),
        self.emailvar.set(row[3]),
        self.genderVar.set(row[4]),
        self.departmentVar.set(row[5]),
        self.adressVar.set(row[6]),
        self.salaryVar.set(row[7]),

    def delete(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.idVar.get()=="":
                messagebox.showerror("Error","Please Enter an ID")
            else:
                cur.execute("Select * from employee where id=?",(self.idVar.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Error")
                else:
                    delmsg = messagebox.askyesno("Confirm","Do you want to delete {} from your database".format(self.nameVar.get()))
                    if delmsg == True:
                        cur.execute("DELETE FROM employee where id=?",(self.idVar.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Employee has been deleted",parent=self.root)
                        self.show
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",)
        self.show()

    def clear(self):
        self.idVar.set(""),
        self.nameVar.set(""),
        self.phoneVar.set(""),
        self.emailvar.set(""),
        self.genderVar.set(""),
        self.departmentVar.set(""),
        self.adressVar.set(""),
        self.salaryVar.set(""),
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
                    cur.execute("select * from employee where "+self.searchbyVar.get()+" LIKE '%"+self.searchVar.get()+"%'")

                    rows = cur.fetchall()
                    if len(rows) != 0:
                        self.employeeTable.delete(*self.employeeTable.get_children())
                        for row in rows:
                            self.employeeTable.insert('',END,values=row)                    
                    else:
                        messagebox.showerror("Error","No record found",parent=self.root)
                con.commit()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{str(ex)}",)
            













        

if __name__=="__main__":

    root=Tk()
    employeeC(root)
    root.mainloop()