#method one

def Count(No):
    counter = 0
    n = 0
     
    while No > 0:
        n = No // 10
        counter += 1
        No = n 


    print("The total number of digits is : ",counter)



def main():
    No = int(input("Enter a Number  : "))
    Count(No)


if __name__ == "__main__":
    main()

#method 2 --- take input of number as a string and use len()


