import os

def main():
    print("enter the file name you want to read : ")

    filename = input()
    ret = os.path.exists(filename)

    if (ret == True):
        print("the file is present in the current directory.")
        fobj = open(filename,"r")
        data =  fobj.read()
        print("Data from file is :" + data)
        fobj.close()

    else:
        print("it is not present in the current directory.")

    
    


if __name__ == "__main__":
    main()