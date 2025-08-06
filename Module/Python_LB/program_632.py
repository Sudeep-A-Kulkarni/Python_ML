def DisplayFactors(iNo):

    iSum = 0

    for i in range(1, (iNo//2)+1):
        if (iNo % i == 0):
            iSum += i

    return iSum 


def main():
    print("Enter a number .")
    iValue = int(input())

    iRet = DisplayFactors(iValue)

    print(f"the sumation of the factors of {iValue} are {iRet}")

if __name__ == "__main__":
    main()