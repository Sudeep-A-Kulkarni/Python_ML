def Maximum(Brr):
    iMax = Brr[0]
    for no in Brr:
        if iMax < no:
            iMax = no
    
    return iMax

    

def main():
    print("Enter the number of elemnets: ")
    iLength = int(input())

    iData = []

    print("enter the list : ")

    for i in range(iLength):
        iValue = int(input())
        iData.append(iValue)


    iRet = Maximum(iData)

    print(f"The addition of elements of {iData} is {iRet}")


    

if __name__ == "__main__":
    main()