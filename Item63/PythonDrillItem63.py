import shutil
import os



def moveFiles(folder):
    if(folder == "a"):
        source=os.listdir(os.path.abspath("./Folder A/"))
        destination = os.path.abspath("./Folder B/")
        folder = "./Folder A/"
    else:
        source=os.listdir(os.path.abspath("./Folder B/"))
        destination = os.path.abspath("./Folder A/")
        folder = "./Folder B/"


    for files in source:
        print ("Moving file:")
        print (os.path.abspath(folder + files))
        shutil.move(os.path.abspath(folder + files), destination)





def main():
    #See where the files are.
    if(os.listdir("./Folder A/")):
        #files are in Folder A
        moveFiles("a")
    else:
        #files are in Folder B
        moveFiles("b")








if __name__ == "__main__": main()
