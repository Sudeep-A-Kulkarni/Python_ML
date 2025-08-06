
def Display(no):
    for i in range(no,0,-1):
        print(i, end = "\t")    


    print(" ")


def main():
    print("Enter a nuber : ")
    iValue= int(input())

    Display(iValue)



if __name__ == "__main__":
    main()