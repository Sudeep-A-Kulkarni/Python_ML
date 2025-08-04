def Factorial(No):
    fact = 1
    for i in range(1,No+1):
        fact = fact * i
    return fact


def main():
    print("Enter a Number :")
    No = int(input())
    ret = Factorial(No)
    print("The Factorial of the given number is :",ret)


if __name__=="__main__":
    main()