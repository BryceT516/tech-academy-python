import sqlite3
import os
from datetime import datetime
import DrillItem66




class DataClass:

    def __init__(self, databaseName):
        self.database = databaseName
        self.createDatabase()



    def createDatabase(self):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE if not exists tbl_copied_files( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    filename TEXT, \
                    directory TEXT, \
                    copy_date timestamp \
                    );")
            conn.commit()
        conn.close()



    def addFile(self, filename, directory):
        conn = sqlite3.connect(self.database)        
        with conn:
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO tbl_copied_files \
                        (filename, directory) VALUES \
                        (?, ?)""", [filename, directory])
        conn.close()
        print("Added " + filename + " to database")
        


    def updateCopyDate(self, filename, directory):
        #updates the filename record with current timestamp
        newDateTime = datetime.today()
        print (newDateTime)
        conn = sqlite3.connect(self.database)        
        with conn:
            cursor = conn.cursor()
            cursor.execute("""UPDATE tbl_copied_files \
                        SET copy_date=? WHERE filename=? AND \
                        directory=?""", [newDateTime, filename, directory])
            conn.commit()
        conn.close()
        print(directory + ", " + filename + " updated")




    def getLastCopyDate(self, filename, directory):
        #Return a datetime of the last copy date for the given filename
        print ("Query directory = " + directory)
        #Query the database:
        conn = sqlite3.connect(self.database)
        with conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT copy_date FROM tbl_copied_files WHERE \
                                directory = ? AND filename = ?""", [directory, filename])
            varData = cursor.fetchone()
            
            if(varData):
                if(varData[0]):
                    returnVal = datetime.strptime(varData[0], "%Y-%m-%d %H:%M:%S.%f")

                else:
                    returnVal = ""
                
            else:
                #If nothing is found, add the filename and return nothing
                returnVal = ""
                self.addFile(filename, directory)

        conn.close()
        return returnVal
        
        

    def printAll(self):
        conn = sqlite3.connect(self.database)
        with conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM tbl_copied_files""")
            varData = cursor.fetchall()

            for data in varData:
                for i in data:
                    print(i)

        conn.close()


    
    
