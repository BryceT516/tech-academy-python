from tkinter import *
from tkinter import ttk

def setup():
    global counter
    counter = 0
    start()

def addText(textBoxTarget):
    #Add a line of text to the text box
    global counter
    print('Button clicked')
    textBoxTarget.insert('end', 'New text. Count = ' + str(counter) + '\n')
    
    counter += 1

def start():
    root = Tk()

    notebook = ttk.Notebook(root)
    notebook.pack()

    frame1 = ttk.Frame(notebook, height=400, width=400)
    frame2 = ttk.Frame(notebook)

    notebook.add(frame1, text = "One")
    notebook.add(frame2, text = "Two")

    textBox = Text(frame1, height=30, width=30)

    button = ttk.Button(frame1, text = 'Click Me!', command=lambda: addText(textBox))

    button.pack()

    textBox.pack()

    root.mainloop()



if __name__ == '__main__':setup()
