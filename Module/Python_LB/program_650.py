def ReverseArray(Brr):
    iStart = 0
    iEnd = len(Brr) - 1
    iTemp = 0
    while (iStart < iEnd):
        Brr[iStart], Brr[iEnd] = Brr[iEnd], Brr[iStart]
        iStart +=1
        iEnd -= 1
            

def main():
    print("Enter the number of elemnets: ")
    iLength = int(input())

    iData = []

    print("enter the list : ")

    for i in range(iLength):
        iValue = int(input())
        iData.append(iValue)

    ReverseArray(iData)

    print(iData)


if __name__ == "__main__":
    main()
