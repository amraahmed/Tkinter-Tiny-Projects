from tkinter import *

root = Tk()
root.title("Click Me")
root.geometry("400x300")

count = 0
size = 26

def contract():

    global count,size

    if count <= 10:
        size -= 2

        mybtn.config(font=("Helvetica",size))
        count-=1

        root.after(100,contract)


def expand():
    global count,size

    if count < 10:
        size += 2

        mybtn.config(font=("Helvetica",size))

        count += 1 
        root.after(100,expand)

    elif count == 10:
        contract()
  

mybtn = Button(root,command=expand,text="Don't Click",font='Helvetiva 24',fg='red',)
mybtn.pack(pady=100)

root.mainloop()