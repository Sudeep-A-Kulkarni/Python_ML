def Display(size):
    for i in range(size):
        for j in range(size):
            print("*",end = " ")
        print("\n")


def main():
    print("enter a number ")
    size = int(input())
    Display(size)


if __name__ =="__main__":
    main()