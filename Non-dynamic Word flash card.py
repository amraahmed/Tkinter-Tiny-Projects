from tkinter import *
from random import randint


root = Tk()
root.title("Flash Card")
root.geometry('550x410')
words = [(('Hola'),('Hello')),
(('Adiós'),('Goodbye')),
(('Porfavor'),('Please')),
(('Gracias'),('Thankyou')),
(('Losiento'),('Sorry')),
(('Salud'),('Blessyou')),
(('Sí'),('Yes')),
(('No'),('No')),
(('¿Quién?'),('Who?')),
(('¿Qué?'),('What?')),
(('¿Porqué?'),('Why?')),
(('¿Dónde?'),('Where?'))]

count = len(words)

def next():
    global rndmwrd
    global hintC,hinter
    hinter= ''
    hintC = 0    
    rndmwrd = randint(0,count-1)
    spanword.config(text=words[rndmwrd][0])
    anslbl.config(text='')
    myent.delete(0,END)
    hntlbl.config(text='')
    

def answer():
    if myent.get().capitalize() == words[rndmwrd][1]:
        anslbl.config(text=f"Correct!, {words[rndmwrd][0]} means {words[rndmwrd][1]}")
    else:
        anslbl.config(text=f"Try again!, {words[rndmwrd][0]} doesn't mean {myent.get().capitalize()}")

hinter= ''
hintC = 0
def hint():
    global hintC
    global hinter

    if hintC < len(words[rndmwrd][1]):
        hinter = hinter + words[rndmwrd][1][hintC]
        hntlbl.config(text=hinter)
        hintC +=1

spanword = Label(root,text='',font='Helvetica 36')
spanword.pack(pady=50)

anslbl = Label(root,text='')
anslbl.pack(pady=20)

myent = Entry(root,font="Helvetica 16")
myent.pack(pady=20)

btnf = Frame(root)
btnf.pack(pady=20)


ansbtn = Button(btnf,text='Answer',command=answer)
ansbtn.grid(row=0,column=0,padx=20)

nxtbtn = Button(btnf,text='Next',command=next)
nxtbtn.grid(row=0,column=1)

hntbtn = Button(btnf,text='Hint',command=hint)
hntbtn.grid(row=0,column=2,padx=20)

hntlbl = Label(root,text='')
hntlbl.pack(pady=20)

next()

root.mainloop()