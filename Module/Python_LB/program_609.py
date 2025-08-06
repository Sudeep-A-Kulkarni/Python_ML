def CheckEvenOdd(no):
    if (no % 2 == 0):
        return True

    else:
        return False

def main():
    print("Enter a number : ")
    value = int(input())

    bRet = CheckEvenOdd(value)
    if (bRet == True):
        print(f"{value} is even number")

    else:
        print(f"{value} is odd number")





if __name__ == "__main__":
    main()