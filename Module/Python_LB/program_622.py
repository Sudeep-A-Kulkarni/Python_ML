def Addition(no):
    isum = 0
    for i in range(no+1):
        isum += i

    return isum


def main():
    print("ENter a number : ")
    value = int(input())
    
    iret = Addition(value)

    print(f"Addition is : {iret}")

if __name__=="__main__":
    main()