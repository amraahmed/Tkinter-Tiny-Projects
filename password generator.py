from tkinter import *
from random import randint

root = Tk()
root.title("Password Generator")
root.geometry("500x300")


password = chr(randint(33,126))

ent4 = IntVar()

def gen():

    # Clear Our Entry Box
     ent2.delete(0,END)
    # Get PW Length and convert to integer
     pw_length = int(ent.get())
    # create a variable to hold our password
     my_password = ''
    # Loop through password length
     for x in range (pw_length):
         my_password += chr(randint(33,126))
         print(my_password)
        

     ent2.insert(0,my_password)


def copy():
    root.clipboard_clear()
    root.clipboard_append(ent2.get())

lf = LabelFrame(root,text='How many characters do you want')
lf.pack(pady=20)

ent = Entry(lf,font='Helvetica 24',textvariable=ent4)
ent.pack(pady=20,padx=20)

ent2 = Entry(root,text='',state=DISABLED,font='Helvetica 26',bd=0,bg='systembuttonface')
ent2.pack(pady=20)

myframe = Frame(root)
myframe.pack(pady=20)

btn = Button(myframe,text='Generate',command=gen)
btn.grid(row=0,column=0,padx=10)

cpy = Button(myframe,text='Copy',command=copy)
cpy.grid(row=0,column=1,padx=10)


root.mainloop()