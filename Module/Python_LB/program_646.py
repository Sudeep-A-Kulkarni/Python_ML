def ReverseArray(Brr):
    Crr = []
    for i in range(len(Brr)-1,-1,-1):
        Crr.append(Brr[i])

    return Crr
    

    

def main():
    print("Enter the number of elemnets: ")
    iLength = int(input())

    iData = []

    print("enter the list : ")

    for i in range(iLength):
        iValue = int(input())
        iData.append(iValue)

    Aret = ReverseArray(iData)
    print("the reverse of the array is : ")

    print(Aret)


    

if __name__ == "__main__":
    main()
