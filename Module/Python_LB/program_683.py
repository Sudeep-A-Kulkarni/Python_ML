def Display(Rows, Columns):
    if Rows != Columns:
        print("Invalid input")
        return
    else:
        for i in range(1,Rows+1):
            print("$\t"*Columns)
            

                
               
                
        
        
        

def main():
    print("Enter a number of rows: ")
    Value1 = int(input())
    print("Enter a number of rows: ")
    Value2 = int(input())   

    Display(Value1, Value2)

if __name__ == "__main__":
    main()