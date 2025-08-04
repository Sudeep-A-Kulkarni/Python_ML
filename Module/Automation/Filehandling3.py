def main():
    print("enter the file name you want to create. ")

    filename = input()

    fobj = open(filename,"w")

    print("enter the data you want to write in file . ")
    data = input()

    fobj.write(data)

    fobj.close()

if __name__ == "__main__":
    main()