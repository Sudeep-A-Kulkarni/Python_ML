def Display(Rows):
    for i in range(1,Rows+1):
        print("*\t"*i)
                        
    print("\n")
        
        

def main():
    print("Enter a number of rows: ")
    Value1 = int(input())
    
    Display(Value1)

if __name__ == "__main__":
    main()
