from tkinter import *
from random import randint
from tkinter import ttk

root = Tk()
root.title("Rock Paper Scissors")
root.geometry('500x600')
root.config(bg='white')




rock = PhotoImage(file=R'C:\Users\ITECH\Downloads\rock1.png',width=400,height=400)
sc = PhotoImage(file=R'C:\Users\ITECH\Downloads\sc.png',width=400,height=400)
pep = PhotoImage(file=R'C:\Users\ITECH\Downloads\pep.png',width=400,height=400)



imglst = [rock,pep,sc]
pcn = randint(0,2)
imglbl = Label(root)
imglbl.pack(pady=20)

def spn():
    pcn = randint(0,2)
    

    chov = 0

    if cho.get == 'rock':
        chov = 0
    elif cho.get == 'pep ':
        chov = 1
    elif cho.get == 'sc':
        chov = 2

    if chov == 0: #rock
        if pcn == 0:
            wnlslbl.config(text="It's a TIE")
        elif pcn == 1:
            wnlslbl.config(text="You Lose")
        elif pcn == 2:
            wnlslbl.config(text="You Win")
    elif chov == 2: #sc
        if pcn == 0:
            wnlslbl.config(text="You LOSE")
        elif pcn == 1:
            wnlslbl.config(text="It's a WIN")
        elif pcn == 2:
            wnlslbl.config(text="TIE")
    elif chov == 1: #pep
        if pcn == 0:
            wnlslbl.config(text="you win")
        elif pcn == 1:
            wnlslbl.config(text="TIE")
        elif pcn == 2:
            wnlslbl.config(text="Tie")
    imglbl.config(image=imglst[pcn])


cho = ttk.Combobox(root,value=("rock","paper","sc"),state="readonly")
cho.current(0)
cho.pack(pady=20)
spnbtn = Button(root,text='Spin',command=spn)
spnbtn.pack(pady=10)

wnlslbl = Label(root,text='',font="Helvetica 24",bg='white')
wnlslbl.pack(pady=50)



root.mainloop()