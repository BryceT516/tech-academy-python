from tkinter import *
from tkinter import ttk

root = Tk()

label = ttk.Label(root, text = "Hello, tkinter") #Original creation of the label
label.pack() #using pack to place the label in the window

label.config(text = "Howdy, Tkinter! It\'s been a while since we last met. "
             "Great to see you again!")
label.config(wraplength = 150)
label.config(justify = CENTER)
label.config(foreground = 'blue', background = 'yellow')
label.config(font = ('courier', 18, 'bold'))

label.config(text = "Howdy, Tkinter!") #Making the text shorter again.

logo = PhotoImage(file = './Ex_Files_Python_Tkinter/Exercise Files/Ch03/python_logo.gif')
label.config(image = logo)
label.config(compound = 'text')
label.config(compound = 'center')
label.img = logo
label.config(image = label.img)
label.config(compound = 'image')

                  
