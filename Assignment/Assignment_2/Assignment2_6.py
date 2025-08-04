def Display(No):
    for i in range(No,0,-1):
        for j in range(i):
            print("*",end = " ")
        print("\n")
        


def main():
    print("Enter a number : ")
    No = int(input())
    Display(No)

if __name__ == "__main__":
    main()