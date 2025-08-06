def ReplaceA(data):
    output = ''
    for ch in data:
        if ch == 'a':
            output.append("_")   #error ...string does not support 
        else:
            output.append(ch)

    return output



def main():
    print("Enter string : ")
    str = input()
    iret = ReplaceA(str)

    print("Updated string is : ")

    print(iret)

    
        



if __name__ == "__main__":
    main()