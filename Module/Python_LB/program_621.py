def Display(no):

    for i in range(1, no + 1):
        print("*", end = "\t")

    print(" ")

def main():
    print("enter a number : ")
    value = int(input())

    Display(value)

if __name__ == "__main__":
    main()