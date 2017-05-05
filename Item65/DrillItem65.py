#!/usr/bin/python3

#Author: Bryce Tucker
#       bryce.tucker@gmail.com


from tkinter import *
from tkinter import ttk
from pathlib import Path
import os
import sys
import shutil
import time
import string

class FileCopier:
    
    def __init__(self, master):
        self.master = master
        self.master.geometry('480x400+200+200')
        self.master.title('File Copier')
        self.master.resizable(False, False)
        self.master.configure(background = '#428bca')

        possibleDrives = []
        for i in string.ascii_uppercase[:26]:
            possibleDrives.append(i + ":/")

        self.availableDrives = []
        for drive in possibleDrives:
            if (self.isDrive(drive)):
                self.availableDrives.append(drive)

        self.startPath = self.availableDrives[0]

        self.sourcePath = self.startPath
        self.destinationPath = self.startPath

        #Set up the treeview selector for the source directory
        self.sourceTree = ttk.Treeview(self.master)

        self.populateTreeview(self.startPath, self.sourceTree, "source")

        self.sourceTree.configure(height=15)
        self.sourceTree.column('#0', width=228)
        self.sourceTree.heading('#0', text='Source Directory')
        
        self.sourceTree.grid(column=0, row=0, padx=5, sticky=(W))
        self.sourceTree.bind('<ButtonRelease-1>', lambda event: self.selectDirectory(event, self.sourceTree))

        scrollbarSource = Scrollbar(self.master)
        scrollbarSource.grid(column = 0, row = 0, sticky=(N, S, E))

        self.sourceTree.configure(yscrollcommand = scrollbarSource.set)

        scrollbarSource.config(command=self.sourceTree.yview)
        
        #Set up the treeview selector for the destination directory
        self.destinationTree = ttk.Treeview(self.master)

        self.populateTreeview(self.startPath, self.destinationTree, "destination")
        self.destinationTree.configure(height=15)
        self.destinationTree.column('#0', width=228)
        self.destinationTree.heading('#0', text='Destination Directory')
        self.destinationTree.grid(column=2, row=0, padx=5, sticky=(E))
        self.destinationTree.bind('<ButtonRelease-1>', lambda event: self.selectDirectory(event, self.destinationTree))

        scrollbarDestination = Scrollbar(self.master)
        scrollbarDestination.grid(column=2, row=0, sticky=(N, S, E) )
        self.destinationTree.configure(yscrollcommand = scrollbarDestination.set)
        scrollbarDestination.config(command=self.destinationTree.yview)

        #Add a button to copy the files
        copyButton = ttk.Button(master, text=">>>>> Copy Recent files >>>>", command=self.copyFiles)
        copyButton.grid(column = 0, columnspan=3, row = 2, pady=10)





        

    def copyFiles(self):
        #Performs the copying of files that have been modified in the last 24 hours.
        
        #print (self.sourcePath)
        #print (self.destinationPath)
        
        currentTime = time.time();
        src = os.path.abspath(self.sourcePath) + "\\"
        dest = os.path.abspath(self.destinationPath)
        source = os.listdir(src)
        copyCount = 0

        for files in source:
            #print(src + files)
            lastModTime = os.path.getmtime(src + files)
            timeSinceLastMod = currentTime - lastModTime
            #print(str(timeSinceLastMod))
            if timeSinceLastMod < 86400 :
                print ("Copy file: " + files + " : modified: " + time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime
                                     (os.path.getmtime(src + files))))
                shutil.copy2(src + files, dest)
                copyCount = copyCount + 1
        
        print ( str(copyCount) + " files copied")
        self.populateTreeview(self.sourcePath, self.sourceTree, "source")
        self.populateTreeview(self.destinationPath, self.destinationTree, "destination")





    def selectDirectory(self, event, tree):
        #Method for when a tree node is selected, changes the tree to list the selected directory's contents
        curItem = tree.focus()
        #print (tree.item(curItem))

        itemDict = tree.item(curItem)
        itemValues = itemDict['values']
        if (itemValues[0] == "file"):
            currentDir = itemValues[1]
        else:
            currentDir = itemValues[0]

        self.populateTreeview(currentDir, tree, itemValues[2])
        
        if (itemValues[2] == "source"):
            self.sourcePath = currentDir
        else:
            self.destinationPath = currentDir
        
        


    def populateTreeview(self, currentDir, tree, treeID):
        #Clear the tree first
        tree.delete(*tree.get_children())

        #Use the passed in current directory path to determine where in the hierarchy
        # this directory is and get the parent directory.
        pathList = currentDir.split('/')
        #print(pathList)
        if (pathList[len(pathList)-1] == ""):
            pathList.pop()
            
        parentDir = ""
        if(len(pathList) > 1):
            #There is at least one parent directory
            for i in range(len(pathList)-1):
                if parentDir == "":
                    parentDir = pathList[i] #This is the top of the hierarchy, no parent directory
                else:
                    parentDir = parentDir + "/" + pathList[i]
                    
        #Add nodes for each directory and file to the selected treeview          
        itemList = []
        try:
            itemList = os.listdir(currentDir) #Get the list of items in the directory
                    
        except IOError as e: #Dealing with exceptions such as permission errors.
            errno, strerror = e.args
            print ("I/O error({0}): {1}".format(errno, strerror))
        except:
            print("Unexpected error:", sys.exc_info()[0])

        
        if (parentDir != ""):
            parentDirNode = tree.insert("", "0", text="..", values=(parentDir, "", treeID)) #Provide a way to get to the parent directory
        else:
            for drive in self.availableDrives:
                tree.insert("", "0", text=drive, values=(drive, "", treeID)) #List the drives available for selection

        cRoot = tree.insert("", "end", text=pathList[len(pathList)-1], value=(currentDir, parentDir, treeID))
        tree.item(cRoot, open=True)
        for node in itemList:
            nodePath = os.path.abspath(currentDir + "/" + node)
            #print(nodePath)
            try:
                isDirectory = os.path.isdir(nodePath)
                if isDirectory:
                    #Adding a '+' to the text of the node to indicate a difference between directories and files.
                    dirNode = tree.insert(cRoot, "end", text="+"+node, values=(currentDir + "/" + node, currentDir, treeID))
                    
                else:
                    tree.insert(cRoot, "end", text=node, values=("file", currentDir,treeID))
                    
            except IOError as e: #Dealing with exceptions such as permission errors.
                errno, strerror = e.args
                print ("I/O error({0}): {1}".format(errno, strerror))
            except:
                print("Unexpected error:", sys.exc_info()[0])




    def isDrive(self, driveLetter):
        #This method checks to see if the passed in drive letter is a valid directory to use.
        try:
            isDirectory = os.path.isdir(driveLetter)
            if isDirectory:
                return True
                            
            else:
                return False
                            
        except IOError as e:
            errno, strerror = e.args
            print ("I/O error({0}): {1}".format(errno, strerror))
        except:
            print("Unexpected error:", sys.exc_info()[0])        





def main():
    master = Tk()
    fileCopier = FileCopier(master)
    master.mainloop()






if __name__ == "__main__": main()

