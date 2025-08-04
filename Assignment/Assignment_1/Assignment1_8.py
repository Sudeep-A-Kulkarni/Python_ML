def Display(n):
    for i in range(n):
        print("*",end =" ")

def main():
    print("Enter a number : ")
    n =  int(input())
    Display(n)
    
if __name__ == "__main__":
    main()