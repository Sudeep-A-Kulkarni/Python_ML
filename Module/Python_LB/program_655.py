def CountFrequency(data):
    iCount = 0
    for ch in data:
        if (ch == 'a'):
            iCount += 1

    return iCount



def main():
    print("Enter string : ")
    str = input()

    

    iret = CountFrequency(str)

    print(f"Frequency of A in {str} is {iret}")
        



if __name__ == "__main__":
    main()