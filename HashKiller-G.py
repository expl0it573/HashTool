import hashlib
from colorama import Fore, init
from tkinter import *

init()

def clicked():
    userword = txt3.get()
    useralg = txt2.get()
    userhash = txt.get()
    
    wordlist = open(userword,"r",encoding='utf-8', errors='ignore')
    
    for line in wordlist:
        hashpass = hashlib.new (useralg)
        hashpass.update (line.rstrip('\n').encode("utf-8"))
        
        if hashpass.hexdigest() == userhash:
            print (Fore.GREEN + "PassFound", line)
            break
        
        else:
            print (Fore.RED + "PassErr", line)

window = Tk()
window.title("HashKiller v 1.0")

lbl = Label(text = "Welcome!")
lbl.grid(column = 0, row = 1)

lbl1 = Label(text = "Input Hash: ")
lbl1.grid(column = 0, row = 3)

lbl2 = Label(text = "Input Algorithm: ")
lbl2.grid(column = 0, row = 4)

lbl3 = Label(text = "Input PassList: ")
lbl3.grid(column = 0, row = 5)

txt = Entry(window, width=20)
txt.grid(column = 1, row = 3 )

txt2 = Entry(window, width=20)
txt2.grid(column = 1, row = 4 )

txt3 = Entry(window, width=20)
txt3.grid(column = 1, row = 5 )

btn = Button(window, text = "Brute!", command=clicked, width = 10)
btn.grid(column= 1, row = 7)

window.geometry('400x250')
window.mainloop()