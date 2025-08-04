def main():
    print("enter the file name you want to create. ")

    filename = input()

    fobj = open(filename,"x")

if __name__ == "__main__":
    main()