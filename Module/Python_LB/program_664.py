def ReplaceA(data):
    i = 0
    for i in range(len(data)):
        if data[i] =='a':
            data[i] = '_' ##String is immutable ----> ERROR



def main():
    print("Enter string : ")
    str = input()
    iret = ReplaceA(str)

    print("Updated string is : ")

    print(iret)

    
        



if __name__ == "__main__":
    main()