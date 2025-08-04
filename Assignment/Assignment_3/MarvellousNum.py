
def ChkPrime(N):
    count = 0
    for i in range(1,N+1):
        if N % i == 0:
            count += 1

    if count == 2:
        return i
    else:
        print("no")
    
#def main():
   # N= int(input("enter a number"))
   
   # ChkPrime(N)

#if __name__ == "__main__":
#    main()
