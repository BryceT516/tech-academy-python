import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

import phonebook_main
import phonebook_gui




def center_window(self, w, h):
    #Function figures out the center of the screen and places the
    # window in the center
    #Get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    #Calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        #Close the app
        self.master.destroy()
        os._exit(0)


def create_db(self):
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_phonebook( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT \
            );")
        #You must commit() to save changes & close the database connection
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    data = ('John', 'Doe', 'John Doe', '111-111-1111', 'john.doe@gmail.com')
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur, count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_phonebook (col_fname, col_lname, col_fullname, col_phone, col_email) VALUES (?,?,?,?,?)""", (data))
            conn.commit()
    conn.close()


def count_records(cur):
    count=""
    cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
    count = cur.fetchone()[0]
    return cur, count


#Select item in the list box
def onSelect(self, event):
    #This is a bound event
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('phonebook.db')
    with conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT col_fname, col_lname, col_phone, col_email FROM tbl_phonebook WHERE col_fullname = (?)""", [value])
            varBody = cursor.fetchall()
            #This returns a tuple and we can slice it into 4 parts using data[] during the iteration
            for data in varBody:
                onClear(self)
                self.entry_fname.insert(0, data[0])                
                self.entry_lname.insert(0, data[1])                
                self.entry_phone.insert(0, data[2])                
                self.entry_email.insert(0, data[3])


def addToList(self):
    fname_input = self.entry_fname.get()
    lname_input = self.entry_lname.get()
    #Normalize the data to keep it consistent
    fname_input = fname_input.strip() #Remove extra whitespace
    fname_input = fname_input.title() #capitalize the names
    lname_input = lname_input.strip()
    lname_input = lname_input.title()
    fullname_input = fname_input + ' ' + lname_input # build the fullname value
    print ('fullname: ' + fullname_input)
    phone_input = self.entry_phone.get().strip()
    email_input = self.entry_email.get().strip()
    if not "@" or not "." in email_input: #Validation on the email address
        print ('Incorrect email format!')

    if(len(fname_input) > 0) and (len(lname_input)>0) and (len(phone_input)>0) and (len(email_input)>0): #Require entries in all fields
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cursor = conn.cursor()
            #Check the database for the existence of the fullname, if exists, then will alert the user and cancel the add operation
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_phonebook WHERE col_fullname = '{}'""".format(fullname_input))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0: #The fullname was not found in the database, so add the info
                print('Adding the new data...')
                cursor.execute("""INSERT INTO tbl_phonebook (col_fname, col_lname, col_fullname, col_phone, col_email) VALUES (?, ?, ?, ?, ?)""", (fname_input, lname_input, fullname_input, phone_input, email_input))
                self.lst_list1.insert(END, fullname_input) #Add the name to the listbox
                onClear(self)
            else:
                messagebox.showerror("Name Error", "'{}' already exists in the database! Please choose a different name.".format(fullname_input))
                onClear(self)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error", "Please ensure that there is data in all four fields.")
    onRefresh(self)
    
                               

def onDelete(self):
    selected_name = self.lst_list1.get(self.lst_list1.curselection()) #The value of the listbox's current selection
    #Should check to make sure something is selected?
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        #Check to make sure we are not deleting the last record in the database.
        # If the last record is deleted, we will get an error
        cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with " + selected_name + " will be permanently deleted. Are you sure?")
            if confirm:
                conn = sqlite3.connect('phonebook.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_phonebook WHERE col_fullname = '{}'""".format(selected_name))
                onDeleted(self) # Call the function to clear all the input boxes and remove the current selection from the listbox
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time.".format(selected_name))
    conn.close()


def onDeleted(self):
    #clear the textboxes
    onClear(self)
    #Try to remove the deleted item from the listbox, it should still be selected
    try:
        index = self.lst_list1.curselection()[0]
        self.lst_list1.delete(index)
    except IndexError:
        pass


def onClear(self):
    self.entry_fname.delete(0, END)
    self.entry_lname.delete(0, END)
    self.entry_phone.delete(0, END)
    self.entry_email.delete(0, END)




def onRefresh(self):
    #Populate the listbox
    self.lst_list1.delete(0, END)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cur.fetchone()[0]
        i = 0
        while i < count:
            cur.execute("""SELECT col_fullname FROM tbl_phonebook ORDER BY col_lname DESC""")
            varList = cur.fetchall()[i]
            for item in varList:
                self.lst_list1.insert(0, str(item))
                i += 1
    conn.close()


def onUpdate(self):
    try:
        selected = self.lst_list1.curselection()[0] #Index of the selected item
        selected_value = self.lst_list1.get(selected) #Get the text value for the selected item
    except:
        messagebox.showinfo("Missing Selection", "No name was selected from the list. Cancelling update request.")
        return
    #The user is only allowed to make changes to phone and email values
    #To change a name, the entire entry must be deleted and a new entry added
    phone_input = self.entry_phone.get().strip()
    email_input = self.entry_email.get().strip()

    if(len(phone_input) > 0) and (len(email_input)>0): #Require data in phone and email inputs
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cur = conn.cursor()
            #Check to see if any data is changed to be updated
            cur.execute("""SELECT COUNT(col_fullname) FROM tbl_phonebook WHERE col_phone = '{}' AND col_email = '{}' AND col_fullname = '{}'""".format(phone_input, email_input, selected_value))
            count = cur.fetchone()[0]
            print("Count = " + str(count))
            if count == 0: #Either phone or email is different for the selected name, so update the info
                response = messagebox.askokcancel("Update Request", "The information for {} will be changed to: Phone: {}, Email: {}. Select OK to continue.".format(selected_value, phone_input, email_input))
                if response: #The user confirmed the update...
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""UPDATE tbl_phonebook SET col_phone = '{}', col_email = '{}' WHERE col_fullname = '{}'""".format(phone_input, email_input, selected_value))
                        onClear(self)
                        conn.commit()
                else: #The user cancelled the update request...
                    messagebox.showinfo("Update Cancelled", "No changes were made to the database.")
            else: #Neither phone or email has been changed from what is already in the database
                messagebox.showinfo("No Changes Detected", "Neither phone or email information has been changed for " + selected_value + ". No changes made to the database.")
            onClear(self)
        conn.close()
    else: #Either phone or email is blank
        messagebox.showerror("Missing Information", "Please select a name from the list. Then edit the phone or email information before requesting an Update.")
    onClear(self)
    
        
                    










if __name__ == "__main__":
    pass
