#from MarvellousNum.py import ChkPrime # type: ignore
import sys
sys.path.append('C:\\Users\\SUDEEP A KULKARNI\\OneDrive\\Desktop\\Python\\Assignment3\\MarvellousNum')
import MarvellousNum

def ListPrime(Data):
    sum = 0
    for value in Data:
        ret = ChkPrime(value)
        
         


def main():
    print("enter the size of the list : ")
    size = int(input())
    Data= []
    for value in range(size):
        n = int(input())
        Data.append(n)

    ListPrime(Data)

    
if __name__ == "__main__":
    main()