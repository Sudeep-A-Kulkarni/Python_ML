def CountFrequency(data):
    iCount = 0
    pattern = "AEIOUaeiou"

    for ch in data:
        if (ch in pattern):
            iCount += 1
        else:
            pass


    return len(data)-iCount



def main():
    print("Enter string : ")
    str = input()

    

    iret = CountFrequency(str)

    print(f"Frequency of vowels in {str} is {iret}")
        



if __name__ == "__main__":
    main()