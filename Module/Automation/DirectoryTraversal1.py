import os

def main():
    for FolderName, SubFolderNames, FileName in os.walk("Marvellous"):
        print("folder name is : "+FolderName)
        for subf in SubFolderNames:
            print("the sub folder name is : "+subf)
        for fname in FileName:
            print("File name is : "+fname)
        


if __name__ == "__main__":
    main()