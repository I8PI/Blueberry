import os , shutil
def tempDeleter(mypath):
    downloadFilePath = mypath
    files = []
    dirs = []
    for x in os.walk(downloadFilePath):
        print (x)
        files.extend(x[2])
        dirs.extend(x[1])
        break
    print ('Files: ', files)
    print ('Dirs: ', dirs)
    for dir in dirs:
        try:
            shutil.rmtree(downloadFilePath + dir)
            print ('Deleted Directory ', dir)
        except:
            pass
    for file in files:
        try:
            os.unlink(downloadFilePath + file)
            print ('Deleted file', file)
        except:
            pass
        # os.remove("ChangedFile.csv")
mypath = 'C:\Users\hmehta\AppData\Local\Temp' + os.sep;
tempDeleter(mypath)
mypath2 = 'C:\Windows\Temp' + os.sep;
tempDeleter(mypath2)
input('Press ENTER to exit')
