def ChkPrime(No):
    if No == 0:
        print("The Number is neither prime nor composite")

    else:
        check = 0
        for i in range(1,No+1):
            if No % i == 0 :
                check += 1
            else:
                pass 

        if check == 2:
            print("The Number is  Prime Number ")
        else:
            print("The Number is not a Prime Number ")


def main():
    print("Enter a number : ")
    No = int(input())
    ChkPrime(No)

if __name__ == "__main__":
    main()