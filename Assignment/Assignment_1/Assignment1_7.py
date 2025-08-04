def ChkDivisibilty(n):
    if n % 5 == 0:
        print("True")
    else:
        print("False")

def main():
    n = int(input("enter a number : "))
    #ChkDivisibilty(n)
    print(bool(n%5==0))

     

if __name__ == "__main__":
    main()