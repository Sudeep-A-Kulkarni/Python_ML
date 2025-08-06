def CountSMall(data):
    iCount = 0
    for ch in data:
        if (ch >="a" and ch<="z"):
            iCount+=1



    return iCount


def main():
    print("Enter string : ")
    str = input()

    

    iret = CountSMall(str)

    print(f"Frequency of vowels in {str} is {iret}")
        



if __name__ == "__main__":
    main()