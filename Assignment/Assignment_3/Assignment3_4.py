

def Max_Num(Data):
    max = Data[0]
    for value in Data:
        if max > value:
            pass
        else:
            max = value


    return max


def main():
    print("The size of the List : ")
    size = int(input())

    Data = []

    print("Enter the list : ")
    for value in range(size):
        n = int(input())
        Data.append(n)

    ret = Max_Num(Data)
    

    print("The maximum number from the given list is : ",ret)







if __name__ == "__main__":
    main()