from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox

root = Tk()
root.title("Translator")
root.geometry("880x300")

langs = googletrans.LANGUAGES
langlst = list(langs.values())
print(langlst)

def trans():
    trnstxt.delete(1.0,END)
    try:
        for key,value in langs.items():
            if (value == orgcmb.get()):
                lk = key 

        for key,value in langs.items():
            if (value == transcmb.get()):
                lkt = key 

        words = textblob.TextBlob(orgtxt.get(1.0,END))

        words = words.translate(from_lang=lk,to=lkt)

        trnstxt.insert(1.0,words)


    except Exception as e:
        messagebox.showerror("Translator", e)
        


def clear():
    orgtxt.delete(1.0,END)
    trnstxt.delete(1.0,END)
    

orgtxt = Text(root,height=10,width=40)
orgtxt.grid(row=0,column=0,pady=20,padx=10)

transbtn = Button(root,text="Translate",font='Helvetica 24',command=trans)
transbtn.grid(row=0,column=1,padx=10)

trnstxt = Text(root,height=10,width=40)
trnstxt.grid(row=0,column=2,pady=20,padx=10)


orgcmb = ttk.Combobox(root,width=50,value=langlst)
orgcmb.current(21)
orgcmb.grid(row=1,column=0)

transcmb = ttk.Combobox(root,width=50,values=langlst)
transcmb.current(26)
transcmb.grid(row=1,column=2)

clearbtn = Button(root,text="Clear",command=clear)
clearbtn.grid(row=2,column=1)


root.mainloop()