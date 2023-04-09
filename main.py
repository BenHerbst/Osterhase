import time
import random
from functools import partial

print("Willkommen zum Osterhasen")
time.sleep(1)
print("Finde die Eier!")
time.sleep(1)

from tkinter import *
import tkinter
from tkinter import messagebox

class EierHandler():
    eier_count = 0
    used_versuche = 0
    versuche = 20

eier_count = 0
EierHandler.gefunden = 0

master=tkinter.Tk()
master.title("Eier App")
master.geometry("550x275")

def eiGefunden(button):
    if EierHandler.used_versuche >= EierHandler.versuche:
        alleVersuche()
    else:
        if EierHandler.gefunden == eier_count:
            alleJefunden()
        else:
            EierHandler.gefunden += 1
            button["state"] = DISABLED
            button.configure(text="Jefunden")
            print("Ei " + str(EierHandler.gefunden) + " von " + str(eier_count))
            if EierHandler.gefunden == eier_count:
                alleJefunden()

def alleVersuche():
    messagebox.showinfo("Information", "Alle verbraucht!!!")

def alleJefunden():
    messagebox.showinfo("Information", "Alle Eier gefunden!")


def keinEi(button):
    if EierHandler.used_versuche >= EierHandler.versuche:
        alleVersuche()
    else:
        if EierHandler.gefunden == eier_count:
            alleJefunden()
        else:
            EierHandler.used_versuche += 1
            print("Verwendete Versuche: " + str(EierHandler.used_versuche))
            button.destroy()

for row in range(10):
    for col in range(10):
        randomNumber = random.randrange(0, 50)
        if randomNumber == 1:
            eier_count += 1
            button1=tkinter.Button(master, text="Versteck", height= 4, width=13)
            button1.configure(command=partial(eiGefunden, button1))
        else:
            button1=tkinter.Button(master, text="Versteck", height= 4, width=13)
            button1.configure(command=partial(keinEi, button1))
        button1.grid(row=row,column=col)

print(str(eier_count) + " Eier  versteckt")

master.mainloop()