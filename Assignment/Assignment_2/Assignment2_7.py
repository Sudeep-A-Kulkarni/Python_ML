def Display(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(j,end= " ")
        print("\n")

def main():
    n = int(input("enter a number : "))
    Display(n)
    


if __name__ == "__main__":
    main()