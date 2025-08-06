def DisplayFactors(iNo):

    iSum = 0

    for i in range(1, (iNo//2)+1):
        if (iNo % i == 0):
            iSum += i

    return (iSum == iNo)
    

def main():
    print("Enter a number .")
    iValue = int(input())

    iRet = DisplayFactors(iValue)

    if iRet : 
        print(f"{iValue} is a perfect number")

    else:
        print(f"{iValue} not a perfect number")


if __name__ == "__main__":
    main()