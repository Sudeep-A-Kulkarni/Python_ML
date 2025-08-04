def Prime():
    print("enter a number : ")
    No1 = int(input())
    count = 0
    for i in range(1,No1+1):
        if No1 %  i == 0:
            count += 1
        else:
            pass
    
    if count == 2:
        print("the number is a prime number")

    else:
        print("the number is not a prime number ")


#if __name__ == "__main__":
 #   main()