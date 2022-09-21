from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Control Panel")
root.geometry('300x650')

def launch():
    global second
    second = Toplevel()
    second.geometry('200x200')


def widthSl(e):
   
    second.geometry(f"{int(wdthS.get())}x{int(hightS.get())}")

def hightSl(e):
    second.geometry(f"{int(wdthS.get())}x{int(hightS.get())}")

def bthSl(e):
    second.geometry(f"{int(bthS.get())}x{int(bthS.get())}")


lanchbtn = Button(root,text='Launch',command=launch)
lanchbtn.pack(pady=20)

wdthf = LabelFrame(root,text='Width Frame')
wdthf.pack(pady=20)

hightf = LabelFrame(root,text='Height Frame')
hightf.pack(pady=20)

bthf = LabelFrame(root,text='Both')
bthf.pack(pady=20)

wdthS = ttk.Scale(wdthf,from_=100,to=500,orient=HORIZONTAL,length=200,command=widthSl,value=100)
wdthS.pack(pady=20,padx=20)

hightS = ttk.Scale(hightf,from_=100,to=500,orient=VERTICAL,length=200,command=hightSl,value=100)
hightS.pack(pady=20,padx=20)

bthS = ttk.Scale(bthf,from_=100,to=500,orient=HORIZONTAL,length=200,command=bthSl,value=100)
bthS.pack(pady=20,padx=20)



root.mainloop()