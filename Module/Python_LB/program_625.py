def Sum_Digits(no):
    i_digit = 0
    i_sum = 0
    while (no != 0):
        i_digit = no % 10
        i_sum += i_digit
        no = no // 10


    return i_sum


    

def main():
    print("ENter a number : ")
    value = int(input())

    ret = Sum_Digits(value)
    print(f"The sum of the digits is : {ret}")

    
if __name__=="__main__":
    main()