def Factorial(no):
    ifact = 1
    for i in range(1,no+1):
        ifact *= i

    return ifact


def main():
    print("ENter a number : ")
    value = int(input())

    iret = Factorial(value)

    print(f"factorial is : {iret}")
    
if __name__=="__main__":
    main()