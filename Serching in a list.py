from tkinter import *
root = Tk()
root.title("Find me")
root.geometry("500x300")

def update(data):
    lst.delete(0,END)

    for x in data :
        lst.insert(END,x)

def fill(evt):
    ent.delete(0,END)
    ent.insert(0,lst.get(ACTIVE))

def check(e):
    typed = ent.get()
    key = 0
    for x in ent.get():
        key +=1
    if typed == "":
        data = drnks
    else:
        data=[]
       

        for item in drnks:
            if typed.lower()[:key] == item.lower()[:key]:
                data.append(item)

    update(data)

    


mylbl = Label(root,text="Start Typing....",font='Helvetica 14',fg='grey')
mylbl.pack(pady=20)

ent = Entry(root,font='helvetica 20')
ent.pack()

lst = Listbox(root,width=50)
lst.pack(pady=40)

drnks = ['Pepsi','cola','sevev up','Heniken','fanta','sprit','sting']

update(drnks)
lst.bind("<<ListboxSelect>>",fill)

ent.bind("<KeyRelease>",check)

root.mainloop()