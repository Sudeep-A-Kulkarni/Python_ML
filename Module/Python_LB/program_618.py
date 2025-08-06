def Display(no):
    while no > 0 :
        print("*")
        no -= 1

def main():
    print("Enter a number : ")

    value = int(input())

    Display(value)


if __name__ == "__main__":
    main()