from tkinter import *
import tkinter as tk

import phonebook_main
import phonebook_func


def load_gui(self):

        self.frm_main = ttk.Frame(self.master)
        self.frm_main.pack()
        self.frm_main.config(width=460, height=380)

        self.lbl_fname = ttk.Label(self.frm_main, text='First Name:')
        self.lbl_fname.grid(row=0, column=0, sticky=NW)

        self.entry_fname = ttk.Entry(self.frm_main, width = 30)
        self.entry_fname.grid(row=1, column=0, columnspan = 2)

        self.lbl_lname = ttk.Label(self.frm_main, text='Last Name:')
        self.lbl_lname.grid(row=2, column=0, sticky=NW)

        self.entry_lname = ttk.Entry(self.frm_main, width = 30)
        self.entry_lname.grid(row=3, column=0, columnspan = 2)

        self.lbl_phone = ttk.Label(self.frm_main, text='Phone Number:')
        self.lbl_phone.grid(row=4, column=0, sticky=NW)

        self.entry_phone = ttk.Entry(self.frm_main, width = 30)
        self.entry_phone.grid(row=5, column=0, columnspan = 2)

        self.lbl_email = ttk.Label(self.frm_main, text='Email Address:')
        self.lbl_email.grid(row=6, column=0, sticky=NW)

        self.entry_email = ttk.Entry(self.frm_main, width = 30)
        self.entry_email.grid(row=7, column=0, columnspan = 2)

        self.lbl_info = ttk.Label(self.frm_main, text='Information:')
        self.lbl_info.grid(row=0, column=2, columnspan=2, sticky=NW)

        self.scrollbar1 = Scrollbar(self.frm_main, orient=VERTICAL)
        self.lst_list1 = Listbox(self.frm_main, exportselection=0, yscrollcommand=self.scrollbar1.set, width = 30)
        self.lst_list1.bind('<<ListboxSelect>>', lambda event: phonebook_func.onSelect(self, event))
        self.scrollbar1.config(command=self.lst_list1.yview)
        self.scrollbar1.grid(row=1, rowspan = 7, column = 6, sticky=N+E+S)
        self.lst_list1.grid(row=1, rowspan=7, column=2, columnspan = 4, padx=10)

        
        

        self.btn_add = ttk.Button(self.frm_main, text='Add', command=lambda: phonebook_func.addToList(self))
        self.btn_add.grid(row=9, column=0, pady=10)

        self.btn_update = ttk.Button(self.frm_main, text='Update', command=lambda: phonebook_func.onUpdate(self))
        self.btn_update.grid(row=9, column=1, pady=10)

        self.btn_delete = ttk.Button(self.frm_main, text='Delete', command=lambda: phonebook_func.onDelete(self))
        self.btn_delete.grid(row=9, column=2, pady=10)

        self.btn_close = ttk.Button(self.frm_main, text='Close', command=lambda: phonebook_func.ask_quit(self))
        self.btn_close.grid(row=9, column=4, columnspan = 3, pady=10)

        phonebook_func.create_db(self)
        phonebook_func.onRefresh(self)


if __name__ == "__main__":
    pass

