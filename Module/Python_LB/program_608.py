def Addition(no1, no2):
    Sum = 0
    Sum = no1 + no2
    return Sum

def main():
    print("Enter first number : ")
    value1 = int(input())

    print("Enter second number : ")
    value2 = int(input())

    Ans = 0
    Ans = Addition(value1, value2)

    print(f"The addition of {value1} and {value2} is : {Ans}")



if __name__ == "__main__":
    main()