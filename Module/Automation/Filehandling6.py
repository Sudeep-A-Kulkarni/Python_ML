import os

def main():
    print("enter the file name you want to delete : ")

    filename = input()
    ret = os.path.exists(filename)

    if (ret == True):
        print("the file is present in the current directory.")
        fobj = os.remove(filename)
    else:
        print("it is not present in the current directory.")

    
    


if __name__ == "__main__":
    main()