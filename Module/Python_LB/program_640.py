def Addition(Brr):
    iSum = 0
    for no in Brr:
        iSum += no

    return iSum 

    

def main():
    print("Enter the number of elemnets: ")
    iLength = int(input())

    iData = []

    print("enter the list : ")

    for i in range(iLength):
        iValue = int(input())
        iData.append(iValue)


    iRet = Addition(iData)

    print(f"The addition of elements of {iData} is {iRet}")


    

if __name__ == "__main__":
    main()