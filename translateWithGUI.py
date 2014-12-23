#Tkinger GUI for translations

import i18nTranslate as translator

tr = translator.jsonTranslate()
from Tkinter import *

def translate():
   data = tr.translate(e1.get(),e4.get() ,e2.get())
   out = e3.get()
   if not out == '':
       tr.writeFile(data, out)

master = Tk()
master.wm_title("Python i18n automatic translator")

Label(master, text="File to translate: ").grid(row=0)
Label(master, text="Output File: ").grid(row=2)
Label(master, text="Input Language").grid(row=6)
Label(master, text="Target Language").grid(row=4)

e1 = Entry(master)
e1.config(width = 75)

e3 = Entry(master)
e3.config(width = 75)

e2 = Entry(master)
e2.config(width = 6)

e4 = Entry(master)
e4.config(width = 6)


e1.grid(row=0, column=1)
e2.grid(row=4, column=1)
e3.grid(row=2, column=1)
e4.grid(row=6, column=1)


Button(master, text='Quit', command=master.quit).grid(row=7, column=0, sticky=W, pady=4)
Button(master, text='Translate', command=translate).grid(row=7, column=1, sticky=W, pady=4)


mainloop()