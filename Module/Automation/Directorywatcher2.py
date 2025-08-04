import os

def main():
    print("enter the name of the directory : ")

    DirName = input()

    ret = os.path.isabs(DirName)

    if (ret == True):
        print("Input is absolute path ")

    else:
        print("Input is relative path")
        NewPath = os.path.abspath(DirName)
        print("The Absolute path is : ",NewPath)




if __name__ == "__main__":
    main()


#Absolute path
#C:\Users\SUDEEP A KULKARNI\OneDrive\Desktop\Python\Automation\Marvellous\Ai>

#relative path
#Python\Automation\Marvellous\Ai>
