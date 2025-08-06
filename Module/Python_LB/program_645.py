def ReverseArray(Brr):
    i = 0
    for i in range(len(Brr)-1,-1,-1):
        print(Brr[i])
    

    

def main():
    print("Enter the number of elemnets: ")
    iLength = int(input())

    iData = []

    print("enter the list : ")

    for i in range(iLength):
        iValue = int(input())
        iData.append(iValue)

    ReverseArray(iData)


    

if __name__ == "__main__":
    main()
