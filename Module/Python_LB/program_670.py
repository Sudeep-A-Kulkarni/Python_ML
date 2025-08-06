def Display(no):
    for i in range(no):
        for j in range(no):
            print("*",end = "\t")
        print("\n")
    
        

def main():
    print("Enter a number : ")
    iValue = int(input())

    Display(iValue)

if __name__ == "__main__":
    main()