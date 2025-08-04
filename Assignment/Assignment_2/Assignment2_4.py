def SumofFactors(No):
    sum = 0
    for i in range(1,No):
        if No % i == 0:
            sum = sum + i
        else:
            pass
    return sum 
            


def main():
    print("Enter a Number : ")
    No = int(input())
    ret = SumofFactors(No)
    print("The Sum of Factors is :",ret)



if __name__ =="__main__":
    main()