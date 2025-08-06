def CheckDivisible(no):
    if (no % 3 == 0) and (no % 5 == 0):
        return True

    else:
        return False

def main():
    print("Enter a number : ")
    value = int(input())

    bRet = CheckDivisible(value)
    if (bRet == True):
        print(f"{value} is divisiible by 3 and(or) 5")

    else:
        print(f"{value} is not divisible by 3 and(or) 5")





if __name__ == "__main__":
    main()