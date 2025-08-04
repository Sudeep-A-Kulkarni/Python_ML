def Number(n):
    if n > 0 :
        print("Positive Number")
    elif n < 0:
        print("Negative Number")
    else:
        print("The number is 0")

def main():
    print("Enter a number : ")
    n = int(input())
    Number(n)


if __name__ == "__main__":
    main()