def Repeat(List, a):
    count = 0
    for value in List:
        if value == a :
            count += 1
        else:
            pass 

    return count
        

def main():
    print("the size of the list is : ")
    size = int(input())

    Data = []

    print("Enter the List : ")

    for value in range(size):
        n = int(input())
        Data.append(n)

    print("Enter a number to find the repition :")
    No1 = int(input())

    ret = Repeat(Data,No1)

    print(f"the number of times {No1} has repeated is : {ret}")


    






if __name__ == "__main__":
    main()
