def ChkNum(n):
    if n%2==0:
        print("Even Number")
    else:
        print("Odd Number")

def main():
    print("enter a number : ")
    n = int(input())
    ChkNum(n)

if __name__ =="__main__":
    main()