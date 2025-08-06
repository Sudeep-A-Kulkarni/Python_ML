def Division(no1, no2):
    Ans = 0
    Ans = no1 // no2                #Floor Division
    

    return Ans
    
    
    
def main():
    print("Enter first number : ")
    value1 = int(input())
    print("Enter second number : ")
    value2 = int(input())

    iRet = Division(value1,value2)

    print(f"Divison of {value1} and {value2} : {iRet}")


    





if __name__ == "__main__":
    main()