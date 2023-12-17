from msilib.schema import CheckBox
import random
from tkinter import *
import tkinter


# creating a window.
window = Tk()

# providing the title of the window.
window.title("Random Password Generator - Scaler Topics")

# setting the size of the window.
window.geometry("600x600")

# adding a label
Label(window, font=('bold', 8), text='Generate Password').pack()


# converting the length into an integer.
length1 = tkinter.IntVar()
length2 = tkinter.IntVar()
length3 = tkinter.IntVar()
length4 = tkinter.IntVar()
length5 = tkinter.IntVar()



# function to generate random password
def passwordGeneration(n):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_'

    # generating random password ans strong it
    password = ''.join(random.sample(characters, n))

    # creating a label and adding the password on the label
    l = Label(window, text=password, font=('bold', 15))  # displaying password
    l.place(x=225, y=65)


# getLength function will call the passwordGeneration function
def getLength():
    if length1.get() == 4:
        passwordGeneration(4)
    elif length2.get() == 6:
        passwordGeneration(6)
    elif length3.get() == 8:
        passwordGeneration(8)
    elif length4.get() == 10:
        passwordGeneration(10)
    else:
        passwordGeneration(12)


# creating buttons
Button(window, text='Generate Password', font=('normal', 10),
       bg='green', command=getLength).place(x=230, y=100)


# creating checkboxes
Checkbutton(text='4 character', onvalue=4, offvalue=0,
            variable=length1).place(x=250, y=150)
Checkbutton(text='6 character', onvalue=6, offvalue=0,
            variable=length2).place(x=250, y=170)
Checkbutton(text='8 character', onvalue=8, offvalue=0,
            variable=length3).place(x=250, y=190)
Checkbutton(text='10 character', onvalue=10, offvalue=0,
            variable=length4).place(x=250, y=210)
Checkbutton(text='12 character', onvalue=12, offvalue=0,
            variable=length4).place(x=250, y=230)


window.mainloop()
