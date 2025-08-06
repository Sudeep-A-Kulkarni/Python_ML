class Demo:
    def __init__(self, A = 0, B = 0):
        self.no1 = A
        self.no2 = B

        print("Inside Consturctor...")
    def __del__(self):
        print("Inside Desturctor...")


    def Display(self):
        print("Value of no1 is : ",self.no1)
        print("Value of no2 is : ", self.no2)

def main():
    print("Inside Main...")
    obj1 = Demo()
    obj2 = Demo()

    obj1.Display()
    obj2.Display()

    print("End of Main.")


if __name__ == "__main__":
    main()