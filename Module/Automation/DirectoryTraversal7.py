import os
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
            #print("file name is : ",fname)
            if (os.path.getsize(os.path.join(FolderName,fname))== 0):
                print("the files having 0 byte are : ",fname)
            
   
                
                
                
def main():
    print("enter the directory you want to traverse: ")
    DirName = input()
    DirectoryWatcher(DirName)
     

        


if __name__ == "__main__":
    main()