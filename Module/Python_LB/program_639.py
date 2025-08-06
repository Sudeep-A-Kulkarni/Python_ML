
def main():
    print("Enter the number of elemnets: ")
    iLength = int(input())

    iData = []

    print("enter the list : ")

    for i in range(iLength):
        iValue = int(input())
        iData.append(iValue)

    print("The entered data is : ")


    print(iData)

if __name__ == "__main__":
    main()