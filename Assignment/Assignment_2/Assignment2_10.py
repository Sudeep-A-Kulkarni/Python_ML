
def Count(No):
    counter = 0
    n = 0
    z = 0
    sum = 0
     
    while No > 0:
        n = No // 10
        z = No % 10
        sum += z
        No = n 

    print("The sum of number is ",sum)


def main():
    No = int(input("Enter a Number  : "))
    Count(No)


if __name__ == "__main__":
    main()



