def Update(Brr):
    
    for i in range(len(Brr)-1,-1,-1):
        if (Brr[i] %2 == 0):
            Brr[i] = Brr[i] + 1
            

def main():
    print("Enter the number of elemnets: ")
    iLength = int(input())

    iData = []

    print("enter the list : ")

    for i in range(iLength):
        iValue = int(input())
        iData.append(iValue)

    Update(iData)

    print(iData)


if __name__ == "__main__":
    main()
