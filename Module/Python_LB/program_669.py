def Display(no):
    for i in range(no, 0, -1):
        print(i,end = "\t")
    for i in range(2,no+1):
        print(i, end = "\t")

def main():
    print("Enter a number : ")
    iValue = int(input())

    Display(iValue)

if __name__ == "__main__":
    main()