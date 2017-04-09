#!/usr/bin/python3
# feedback_template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Feedback:
    def submitForm(self):
        nameInput = self.entryName.get()
        emailInput = self.entryEmail.get()
        commentsInput = self.txtComments.get(1.0, 'end')
        
        print('Name: ' + nameInput)
        print('Email: ' + emailInput)
        print('Comments: ' + commentsInput)

        self.clearForm()

        messagebox.showinfo(title="Explore California Feedback", message="Comments were submitted!")
        


    def clearForm(self):
        self.entryName.delete(0, 'end')
        self.entryEmail.delete(0, 'end')
        self.txtComments.delete(1.0, 'end')

    def __init__(self, master):    
        master.geometry('480x400+200+200')
        master.title('Explore California Feedback Form')
        master.resizable(False, False)
        master.configure(background = '#e1d8b9')

        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#e1d8b9')
        self.style.configure('TButton', background = '#e1d8b9')
        self.style.configure('TLabel', background = '#e1d8b9', font=('Arial', 11)) #Style for the labels
        self.style.configure('Header.TLabel', font=('Arial', 18, 'bold')) #Style for the header text
        
        self.logo = PhotoImage(file = 'tour_logo.gif')

        self.frame1 = ttk.Frame(master)
        self.frame1.pack()

        self.logoLabel = ttk.Label(self.frame1)
        self.logoLabel.config(image=self.logo)
        self.logoLabel.grid(row = 0, column = 0, rowspan = 2)

        self.pageTitle = ttk.Label(self.frame1, text = "Feedback Form", style='Header.TLabel')
        self.pageTitle.grid(row = 0, column = 1, columnspan=2)

        self.instructions = ttk.Label(self.frame1, text = ("Thanks for taking a moment "
                                 "to tell us about your experience. We really"
                                 " appreciate it!"), wraplength = 300)
        self.instructions.grid(row = 1, column = 1, columnspan=2)

        self.lblName = ttk.Label(self.frame1, text="Name:")
        self.lblName.grid(row=2, column = 0, sticky=E)

        self.entryName = ttk.Entry(self.frame1, width = 53, font=('Arial', 10))
        self.entryName.grid(row=2, column=1, columnspan=2, sticky = W)

        self.lblEmail = ttk.Label(self.frame1, text="Email:")
        self.lblEmail.grid(row=3, column = 0, sticky=E, pady=5)

        self.entryEmail = ttk.Entry(self.frame1, width = 53, font=('Arial', 10))
        self.entryEmail.grid(row=3, column=1, columnspan=2, sticky = W , pady=5)

        self.lblComments = ttk.Label(self.frame1, text="Comments:")
        self.lblComments.grid(row=4, column = 0, sticky=NE, pady=5)

        self.txtComments = Text(self.frame1, width = 53, height = 10, wrap='word', font=('Arial', 10))
        self.txtComments.grid(row=4, column=1, columnspan=2, sticky = W , pady=5)

        self.btnSubmit = ttk.Button(self.frame1, text="Submit", command=self.submitForm)
        self.btnSubmit.grid(row=5, column=1, sticky = EW, pady=5, padx=5)

        self.btnClear = ttk.Button(self.frame1, text="Clear", command=self.clearForm)
        self.btnClear.grid(row=5, column=2, sticky = EW, pady=5, padx=5)









        
def main():            
    
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()
    
if __name__ == "__main__": main()
