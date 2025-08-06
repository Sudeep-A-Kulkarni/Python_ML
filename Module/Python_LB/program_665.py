
def ReplaceA(data):
    i = 0
    output = ""

    for ch in data:
        if (ch >= "a" or ch <= "z"): 
            output = output + (ch - 32)    #ERROR
        else:
            output = output+ch

    return output



def main():
    print("Enter string : ")
    str = input()
    iret = ReplaceA(str)

    print("Updated string is : ")

    print(iret)

    
        



if __name__ == "__main__":
    main()