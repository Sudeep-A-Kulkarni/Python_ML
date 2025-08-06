class Demo:
    def __init__(self):
        print("Inside Consturctor...")
    def __del__(self):
        print("Inside Desturctor...")

def main():
    print("Inside Main...")
    obj1 = Demo()
    obj2 = Demo()

    print("End of Main.")


if __name__ == "__main__":
    main()