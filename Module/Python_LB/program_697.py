class Node:
    def __init__(self, no):
        self.data = no
        self.next = None
################################################################################################
class SinglyLL:
    def __init__(self):
        self.first = None
        self.iCount = 0
################################################################################################
    def InsertFirst(self, no):
        newn = Node(no)
        if (self.first == None):            ##LL is empty
            self.first = newn
        else:                               ##LL contains atleast one node
            newn.next = self.first
            self.first = newn

        self.iCount += 1

################################################################################################
    def Display(self):
        pass

#################################################################################################

    def Count(self):
        return self.iCount
#################################################################################################
def main():
    print("Demonstration of Linked List .")

    Sobj = SinglyLL()
    Sobj.InsertFirst(51)
    Sobj.InsertFirst(21)
    Sobj.InsertFirst(11)

    iRet = Sobj.Count()
    print(f"number of nodes in linked list are : {iRet}")


#################################################################################################


if __name__ == "__main__":
    main()

#################################################################################################