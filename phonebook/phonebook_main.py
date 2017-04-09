# Python Ver: 3.6.1
# Author: Bryce Tucker, bryce.tucker@gmail.com
# Purpose: A program written to learn about Python and Tkinter.
# Tested OS: Windows 10

from tkinter import *
from tkinter import ttk

# Import other project modules
import phonebook_gui
import phonebook_func


# Frame is the Tkinter frame class that this class is inheriting from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500, 300) #Height, width
        self.master.maxsize(500, 300)

        # This CenterWindow method will center our app on the user's screen
        phonebook_func.center_window(self, 500, 300)
        self.master.configure(bg="#f0f0f0") #setting the background color
        # This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner 'X' on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # Load in the Gui widgets from a separate module,
        # keeping your code comparmentalized and clutter free
        phonebook_gui.load_gui(self)

    
    
    
if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()



    
