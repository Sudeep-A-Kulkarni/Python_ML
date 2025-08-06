def Display(Rows):
    for i in range(Rows,0,-1):
        print(" " * (Rows-i), end = '')
        print(" * "*i)
                        
        
        

def main():
    print("Enter a number of rows: ")
    Value1 = int(input())
    
    Display(Value1)

if __name__ == "__main__":
    main()
