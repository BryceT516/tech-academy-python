from tkinter import *
from tkinter import ttk

root = Tk()
root.option_add('*tearOff', False)

menubar = Menu(root)
root.config(menu = menubar)
file = Menu(menubar)
edit = Menu(menubar)
help_ = Menu(menubar)
menubar.add_cascade(menu = file, label = 'File')
menubar.add_cascade(menu = edit, label = 'Edit')
menubar.add_cascade(menu = help_, label = 'Help')

file.add_command(label = 'New', command = lambda: print('New File'))
file.add_separator()
file.add_command(label = 'Open', command = lambda: print('Open File'))
file.add_command(label = 'Save', command = lambda: print('Save File'))

file.entryconfig('New', accelerator = 'Ctrl + N')


treeview = ttk.Treeview(root)

treeview.pack()

treeview.insert('', '0', 'item1', text='First Item')
treeview.insert('', '1', 'item2', text='Second Item')
treeview.insert('', '2', 'item3', text='Third Item')


logo= PhotoImage(file='./Ex_Files_Python_Tkinter/Exercise Files/Ch05/python_logo.gif').subsample(10, 10)

treeview.insert('item2', 'end', 'python', text = 'Python', image = logo)


file.entryconfig('Open', image = logo, compound = 'left')

edit.add_command(label = 'Copy', command = lambda: print('Copy'))

edit.entryconfig('Copy', state = 'disabled')

save = Menu(file)
file.add_cascade(menu = save, label='Save')
save.add_command(label='Save as', command = lambda: print('Save as...'))
