import os
def DirectoryWatcher(DirectoryName = "Marvellous"):
        
        flag = os.path.isabs(DirectoryName)
        if (flag == False):
             DirectoryName = os.path.abspath(DirectoryName)
            
             print("absolute path is : "+DirectoryName)

        flag = os.path.exists(DirectoryName)
        if (flag == False):
            print("The path is incalid .")
            exit()

        flag = os.path.isdir(DirectoryName)
        if (flag == False):
             print("Path is valid but the target is not a directory. ")
             exit()

                      


        for FolderName, SubFolderNames, FileName in os.walk(DirectoryName):
            print("folder name is : "+FolderName)
            for subf in SubFolderNames:
                print("the sub folder name is : "+subf)
            for fname in FileName:
                print("File name is : "+fname)


def main():
    print("enter the directory you want to traverse: ")
    DirName = input()
    DirectoryWatcher(DirName)
     

        


if __name__ == "__main__":
    main()