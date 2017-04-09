from tkinter import *
from tkinter import ttk

root = Tk()

breakfast = StringVar()

label = ttk.Label(root, textvariable = breakfast)
label.pack()

ttk.Radiobutton(root, text = 'SPAM', variable = breakfast, value = 'SPAM').pack()
ttk.Radiobutton(root, text = 'Eggs', variable = breakfast, value = 'Eggs').pack()
ttk.Radiobutton(root, text = 'Bacon', variable = breakfast, value = 'Bacon').pack()
ttk.Radiobutton(root, text = 'Sausage', variable = breakfast, value = 'Sausage').pack()
ttk.Radiobutton(root, text = 'Pancakes', variable = breakfast, value = 'Pancakes').pack()
