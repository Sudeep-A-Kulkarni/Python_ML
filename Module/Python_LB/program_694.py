class Node:
    def __init__(self, no):
        self.data = no
        self.next = None

def main():
    print("Demonstration of Linked List .")

    obj1 = Node(11)
    obj2 = Node(21)
    obj3 = Node(51)

    obj1.next = obj2
    obj2.next = obj3
    obj3.next = None




if __name__ == "__main__":
    main()