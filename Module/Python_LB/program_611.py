def Maximum(no1, no2, no3):
    if (no1 > no2) and (no1 > no3):
        return no1
    elif (no2 > no1) and (no2 > no3):
        return no2
    elif (no3 > no1) and (no3 > no2):
        return no3
    else:
        print("All numbers are equal.")
    
def main():
    print("Enter first number : ")
    value1 = int(input())
    print("Enter second number : ")
    value2 = int(input())
    print("Enter third number : ")
    value3 = int(input())


    iRet = Maximum(value1,value2,value3)

    print(f"{iRet} is the maximum number.")


    





if __name__ == "__main__":
    main()