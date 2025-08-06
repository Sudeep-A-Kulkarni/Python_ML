class Arithmatic:
    def __init__(self, A = 0, B = 0):
        self.no1 = A
        self.no2 = B

        print("Inside Consturctor...")      

    def Addition(self):
        return self.no1 + self.no2


    def Subtraction(self):
        return self.no1 - self.no2



def main():
    print("Inside Main...")
    obj1 = Arithmatic(11,10)

    iret = obj1.Addition()

    print(f"Addition is : {iret}")
    iret = obj1.Subtraction()

    print(f"Subtraction is : {iret}")


if __name__ == "__main__":
    main()