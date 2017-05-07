#!/usr/bin/python3

#Author: Bryce Tucker
#       bryce.tucker@gmail.com


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from pathlib import Path
import os
import sys
import shutil
import datetime
import time
import string
from DataLayer import *


class FileCopier:
    
    def __init__(self, master):
        self.db = DataClass("filecopier.db")
        self.db.printAll()
        
        self.master = master
        self.master.geometry('490x550+200+200')
        self.master.title('File Copier')
        self.master.resizable(False, False)
        self.master.configure(background = '#428bca')

        self.source = StringVar()
        self.destination = StringVar()

        Label(self.master, text="Source Directory:").grid(column=0, row=0, sticky=(W))
        
        sourceLabel = Entry(self.master, textvariable=self.source, width=80)
        sourceLabel.grid(column=0, row=1, columnspan=2)

        self.browseSource = Button(self.master, text="Browse Source", command=self.loadFileSource)
        self.browseSource.grid(column=1, row=0)
        

        #Set up the treeview selector for the source directory
        self.sourceTree = ttk.Treeview(self.master)

        self.sourceTree["columns"]=("mod", "copied")
        self.sourceTree.column("mod", width=160)
        self.sourceTree.column("copied", width=160)
        self.sourceTree.heading("mod", text="Last Modified")
        self.sourceTree.heading("copied", text="Last Copied")

        self.sourceTree.configure(height=15)
        self.sourceTree.column('#0', width=160)
        self.sourceTree.heading('#0', text='Source Directory')
        
        self.sourceTree.grid(column=0, columnspan=2, row=2, padx=5, sticky=(E, W))

        scrollbarSource = Scrollbar(self.master)
        scrollbarSource.grid(column = 1, row = 2, sticky=(N, S, E))

        self.sourceTree.configure(yscrollcommand = scrollbarSource.set)

        scrollbarSource.config(command=self.sourceTree.yview)
        


        #Add a button to copy the files
        copyButton = ttk.Button(master, text="vvvvv Copy Recently Modified Files vvvvv", command=self.copyFiles)
        copyButton.grid(column = 0, columnspan=2, row = 3, pady=10)



        #Means to select a destination folder:
        Label(self.master, text="Destination Directory:").grid(column=0, row=4, sticky=(W))
        
        destinationLabel = Entry(self.master, textvariable=self.destination, width=80)
        destinationLabel.grid(column=0, row=5, columnspan=2)

        self.browseDestination = Button(self.master, text="Browse For Destination", command=self.loadFileDestination)
        self.browseDestination.grid(column=1, row=4)





    def loadFileSource(self):
        self.fnameSource = askdirectory()
        self.source.set(self.fnameSource)
        self.populateTreeview()

    def loadFileDestination(self):
        self.fnameDestination = askdirectory()
        self.destination.set(self.fnameDestination)
        

    def copyFiles(self):
        #Performs the copying of files that have been modified in the last 24 hours.

        if(self.destination.get() == ""):
            messagebox.showerror("No Destination Directory Selected", "Please select a destination directory to copy files into.")
        else:
            currentTime = time.time();
            currentDir = self.source.get()

            currentPath = os.path.abspath(currentDir)+"\\"

            itemList = os.listdir(currentPath)
            copyCount = 0

            for files in itemList:
                print(currentPath + files)
                lastCopiedTime = self.db.getLastCopyDate(files, currentDir)
                if(not isinstance(lastCopiedTime,datetime)):
                    #File hasn't been copied before
                    shutil.copy2(currentPath + files, self.destination.get())
                    copyCount = copyCount + 1
                    self.db.updateCopyDate(files, currentDir)
                else:
                    lastModTime = datetime.fromtimestamp(os.path.getmtime(currentPath + files))
                    
                    if (lastCopiedTime < lastModTime):
                        shutil.copy2(currentPath + files, self.destination.get())
                        copyCount = copyCount + 1
                        self.db.updateCopyDate(files, currentDir)
            
            print ( str(copyCount) + " files copied")
            self.populateTreeview()
            messagebox.showinfo("Files copied", str(copyCount) + " files copied")
            



       


    def populateTreeview(self):
        #Clear the tree first
        self.sourceTree.delete(*self.sourceTree.get_children())

        #Use the passed in current directory path to determine where in the hierarchy
        # this directory is and get the parent directory.
                #Add nodes for each directory and file to the selected treeview          
        
        currentDir = self.source.get()

        currentPath = os.path.abspath(currentDir)+"\\"

        
        try:
            itemList = os.listdir(currentPath) #Get the list of items in the directory
                    
        except IOError as e: #Dealing with exceptions such as permission errors.
            errno, strerror = e.args
            print ("I/O error({0}): {1}".format(errno, strerror))
        except:
            print("Unexpected error:", sys.exc_info()[0])

        print (itemList)
        
        for node in itemList:
            nodePath = os.path.abspath(currentDir + "/" + node)

            try:
                isDirectory = os.path.isdir(nodePath)
                if isDirectory:
                    #don't add
                    pass
                else:
                    if (node.endswith(".txt")):
                        #Text file, so list it.
                        lastModTime = os.path.getmtime(nodePath)
                        lastModTimeDisplay = time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime(lastModTime))
             
                        
                        lastCopiedTime = self.db.getLastCopyDate(node, currentDir)
                        if(isinstance(lastCopiedTime,datetime)):
                            lastCopiedTimeDisplay = lastCopiedTime.strftime("%a, %d %b %Y %H:%M:%S")
                            if(lastCopiedTime < datetime.fromtimestamp(lastModTime)):
                                tagsVal = ('copy')
                            else:
                                tagsVal = ()
                        else:
                            lastCopiedTimeDisplay = "Never Copied"
                            tagsVal = ('copy')

                        self.sourceTree.insert("", "end", text=node, values=(lastModTimeDisplay, lastCopiedTimeDisplay), tags=tagsVal)
                        
                    else:
                       #Not a text file, so don't display it.
                       pass

                    
            except IOError as e: #Dealing with exceptions such as permission errors.
                errno, strerror = e.args
                print ("I/O error({0}): {1}".format(errno, strerror))
            except:
                print("Unexpected error:", sys.exc_info()[0])

            self.sourceTree.tag_configure('copy', background='green')
            



def main():
    master = Tk()
    fileCopier = FileCopier(master)
    master.mainloop()






if __name__ == "__main__": main()

