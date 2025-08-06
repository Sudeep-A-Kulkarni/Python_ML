def Display(no):
    while no > 0 :
        print("*", end = "\t")
        no -= 1

    print("\n")

def main():
    print("Enter a number : ")

    value = int(input())

    Display(value)


if __name__ == "__main__":
    main()