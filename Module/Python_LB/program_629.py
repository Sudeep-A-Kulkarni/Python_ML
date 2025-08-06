def Display_Repitition(no):
    iCount_4 = 0
    iCount_5 = 0
    iCount_7 = 0
    iDigit = 0
    while (no != 0):
        iDigit = no % 10
        if (iDigit == 5):
            iCount_5 += 1
        elif (iDigit== 4):
            iCount_4 += 1
        elif (iDigit == 7):
            iCount_7 += 1

        no = no // 10

    return iCount_4, iCount_5, iCount_7


def main():
    print("Enter a number : ")
    iValue = int(input())
    

    iRet_4, iRet_5, iRet_7 = Display_Repitition(iValue)

    print(f"frequwncy of 4 , 5, 7 in {iValue} is {iRet_4}, {iRet_5}, {iRet_7} respectively.")


if __name__ == "__main__":
    main()