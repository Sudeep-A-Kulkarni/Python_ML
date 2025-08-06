def ReplaceA(data):
    output = ''
    for ch in data:
        if ch == 'a':
            output = output + '_' 
        else:
            output = output + ch

    return output



def main():
    print("Enter string : ")
    str = input()
    iret = ReplaceA(str)

    print("Updated string is : ")

    print(iret)

    
        



if __name__ == "__main__":
    main()