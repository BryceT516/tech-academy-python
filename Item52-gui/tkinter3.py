from tkinter import *
from tkinter import ttk

root = Tk()

button = ttk.Button(root, text = 'Click me!')

button.pack()

def callback():
    print('clicked')

button.config(command = callback)

button.invoke()


button.state(['disabled'])

print (button.instate(['disabled'])) #instate checks the state of the button

button.state(['!disabled'])

#Can also put an image on the button.

# Can make images smaller by using subsample



