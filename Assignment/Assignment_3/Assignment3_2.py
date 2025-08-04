def main():
    print("Enter the size of the list : ")
    size = int(input())


    Data=[]


    for value in range(size):
        n = int(input())
        Data.append(n)


    print("the entered string is  : ")


    for value in Data:
        print(value)

    


if __name__ =="__main__":
    main()