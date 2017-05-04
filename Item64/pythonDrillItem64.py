import shutil
import os
import time



def main():
    #Copy files that have been modified in the last 24 hours.
    source=os.listdir(os.path.abspath("./local/"))

    currentTime = time.time();
    src = os.path.abspath("./local/") + "/"
    dest = os.path.abspath("./remote/")
    copyCount = 0
    
    for files in source:
        lastModTime = os.path.getmtime(src + files)
        timeSinceLastMod = currentTime - lastModTime
        if timeSinceLastMod < 86400 :
            print ("Copy file: " + files + " : modified: " + time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime
                                 (os.path.getmtime(src + files))))
            shutil.copy2(src + files, dest)
            copyCount = copyCount + 1
    
    print ( str(copyCount) + " files copied")
            






if __name__ == "__main__": main()
