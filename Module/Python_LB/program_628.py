def Display_Repitition(no):
    iCount = 0
    iDigit = 0
    while (no != 0):
        iDigit = no % 10
        if (iDigit == 5):
            iCount += 1
        else:
            pass
        no = no // 10

    return iCount




def main():
    print("Enter a number : ")
    iValue = int(input())
    

    iRet = Display_Repitition(iValue)

    print(f"frequwncy of 5 in {iValue} is {iRet}")








if __name__ == "__main__":
    main()