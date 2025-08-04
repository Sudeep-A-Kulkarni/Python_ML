import os
import sys
import time 
import hashlib

def CalculateCheckSum(path, BlockSize = 1024):

    fobj = open(path,'rb')

    hobj = hashlib.md5()

    buffer = fobj.read(BlockSize)
    while (len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    fobj.close()

    return hobj.hexdigest()

def DirectoryWatcher(DirectoryName = "Marvellous"):
        
    flag = os.path.isabs(DirectoryName)
    if (flag == False):
         DirectoryName = os.path.abspath(DirectoryName)
            
         print("absolute path is : "+DirectoryName)

    flag = os.path.exists(DirectoryName)
    if (flag == False):
        print("The path is invalid .")
        exit()

    flag = os.path.isdir(DirectoryName)
    if (flag == False):
        print("Path is valid but the target is not a directory. ")
        exit()

                      


    for FolderName, SubFolderNames, FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderName, fname)
            checksum = CalculateCheckSum(fname)
            print("file name : ",fname)
            print("checksum : ",checksum)
            print()


        
   
                
                
                
def main():
    time_stamp = time.ctime()

    filename = "MarvellousLog%s.log" %(time_stamp)
    filename = filename.replace(" ","_")
    filename = filename.replace(":","_")
    
    fobj = open(filename,"w")

    Border = "-"*54

    fobj.write(Border + "\n")
    fobj.write("this is a log file of marvellous sutomation script \n")
  
    fobj.write(Border+ "\n")
    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    fobj.write(Border+ "\n")
    fobj.write("this was created at " + time_stamp + "\n")
    fobj.write(Border+ "\n")

    border = "-"*69
    print(border)
    print("-------------------Marvellous Automations----------------------------")
    print(border)

    # Logic
    if (len(sys.argv) == 2):
        if ((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
            print("this application is used to perform Directory Cleaning.")
            print("this is the directory automation script")

        elif (((sys.argv[1])=="--U") or (sys.argv[1]=="--u")):
            print("Use the given script as .")
            print("ScriptName.py Name_if_Directory")
            print("please provide valid absolute path. ")


        else:
            DirectoryWatcher(sys.argv[1])
            


    else:
        print("use the given flags as : ")
        print("--h : used to display the help.")
        print("--u : used to display the usage.")
        
    print(border)
    print("----------------Thank you for using our script-----------------------")
    print("-------------------Marvellous Infosystems----------------------------")
    print(border)


if __name__ == "__main__":
    main()