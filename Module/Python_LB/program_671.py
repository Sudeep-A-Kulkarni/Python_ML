def Display(Rows, Columns):
    for i in range(no):
        for j in range(no):
            print("*",end = "\t")
        print("\n")
    
        

def main():
    print("Enter a number of rows: ")
    Value1 = int(input())
    print("Enter a number of rows: ")
    Value2 = int(input())   

    Display(Value1, Value2)

if __name__ == "__main__":
    main()