import shutil
import os
import time



def main():
    #Copy files that have been modified in the last 24 hours.
    source=os.listdir(os.path.abspath("./local/"))

    currentTime = time.time();
    
    for files in source:
        lastModTime = os.path.getmtime(os.path.abspath("./local/") + "/" + files)
        timeSinceLastMod = currentTime - lastModTime
        if timeSinceLastMod < 86400 :
            print ("Copy file: " + files + " : modified: " + time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime
                                 (os.path.getmtime(os.path.abspath("./local/") + "/" + files))))
            shutil.copy2(os.path.abspath("./local/") + "/" + files, os.path.abspath("./remote/"))







if __name__ == "__main__": main()
