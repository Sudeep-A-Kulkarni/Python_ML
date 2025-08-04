def main():
    print("Enter the size of elements : ")
    size = int(input())
    print("Enter the list")
    Data = []
    for no in range(size):
        no = int(input())
        Data.append(no)

    sum = 0

    for value in Data:
        sum = sum + value

    print("the sum of all elements is : ",sum)
    

        

if __name__ == "__main__":
    main()