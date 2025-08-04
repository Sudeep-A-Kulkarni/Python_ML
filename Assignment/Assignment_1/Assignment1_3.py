def Add(A, B):
    sum = 0
    sum = A + B
    return sum


def main():
    print("Enter first number")
    No1 = int(input())
    print("Enter second number")
    No2 = int(input())
    ret = Add(No1,No2)
    print("the sum of two numbers is : ",ret)






if __name__ == "__main__":
    main()