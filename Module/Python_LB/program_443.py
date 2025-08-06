def CountEvenOdd(Brr):
    odd_count = 0
    even_count = 0
    for no in Brr:
        if no % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    return even_count, odd_count
    

def main():
    print("Enter the number of elemnets: ")
    iLength = int(input())

    iData = []

    print("enter the list : ")

    for i in range(iLength):
        iValue = int(input())
        iData.append(iValue)


    iEven, iOdd = CountEvenOdd(iData)

    print(f"The addition of elements of {iData} is {iRet}")


    

if __name__ == "__main__":
    main()