def Sum_of_Prime(Data):
    sum = 0
    for value in Data:
        count = 0
        for n in range(1,value+1):
            if value % n == 0 :
                #print("the divisor is ",n)
                count += 1
        #print("the number of divisors are ",count )
        if count == 2:
            sum+=value
        else:
            pass
    print("the sum of prime numbers in this list is : ",sum)

       

def main():
    print("enter the size of the List : ")
    Size = int(input())

    Data = []

    print("Enter the list : ")

    for value in range(Size):
        n = int(input())
        Data.append(n)

    Sum_of_Prime(Data)




if __name__ == "__main__":
    main()