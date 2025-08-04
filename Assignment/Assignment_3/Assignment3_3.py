def main():
    print("Enter the size of the list : ")
    size = int(input())


    Data=[]

    print("Enter the List ")
    for value in range(size):
        n = int(input())
        Data.append(n)

    minimum = Data[0]
    for value in Data:
        if minimum < value :
           pass
        else:
            minimum = value

    print("the minimum value is : ",minimum)



if __name__ =="__main__":
    main()