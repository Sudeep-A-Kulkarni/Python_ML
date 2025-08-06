def Display(Rows, Columns):
    if Rows != Columns:
        print("Invalid input")
        return
    else:
        for i in range(1,Rows+1):
            for j in range(1,Columns+1):
                if ((i == 1) or (i == Rows) or (j == 1) or (j == Columns)) :
                    print("*",end = "\t")
                else:
                    print(" ", end= "\t")  

                
               
                
            print("\n")
        
        

def main():
    print("Enter a number of rows: ")
    Value1 = int(input())
    print("Enter a number of rows: ")
    Value2 = int(input())   

    Display(Value1, Value2)

if __name__ == "__main__":
    main()