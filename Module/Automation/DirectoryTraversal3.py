import os
def DirectoryWatcher(DirectoryName):
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