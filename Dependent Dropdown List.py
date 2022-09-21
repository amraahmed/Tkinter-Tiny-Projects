from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Dependent")
root.geometry("500x400")

sizes = ["small",'medium','large']

smallc = ["red",'green','black']
mediumc = ["white","yellow"]
largec = ["Blue","Grey"]

def pickC(e):
    if combo.get() == "small" :
        combo1.config(value=smallc)
    elif combo.get() == "medium" :
        combo1.config(value=mediumc)
    elif combo.get() == "large" :
        combo1.config(value=largec)

def lstclr(e):
    lst2.delete(0,END)
    if lst.get(ANCHOR) == "small":
        for item in smallc:
            lst2.insert(END,item)
    if lst.get(ANCHOR) == "medium":
        for item in mediumc:
            lst2.insert(END,item)
    elif lst.get(ANCHOR) == "large":
        for item in largec:
            lst2.insert(END,item)






combo = ttk.Combobox(root,value=sizes,state='readonly')
combo.current(0)
combo.pack(pady=20)

combo1 = ttk.Combobox(root,value=[" "],state='readonly')
combo1.current(0)
combo1.pack(pady=20)

combo.bind("<<ComboboxSelected>>",pickC)

framee = Frame(root)
framee.pack(pady=50)

lst = Listbox(framee)
lst2 = Listbox(framee)
lst.grid(row=0,column=0)
lst2.grid(row=0,column=1,padx=20)


for item in sizes:
    lst.insert(END,item)

lst.bind("<<ListboxSelect>>",lstclr)



root.mainloop()