def Display_Digits(no):
    i_digit = 0
    while (no != 0):
        i_digit = no % 10
        print(i_digit, end = "\t")
        
        no = no // 10

    print("")

    

def main():
    print("ENter a number : ")
    value = int(input())

    Display_Digits(value)

    
if __name__=="__main__":
    main()