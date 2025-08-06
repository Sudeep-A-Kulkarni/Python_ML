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
    def InsertLast(self, no):

      
    
        newn = Node(no)
        if (self.first == None):            ##LL is empty
            self.first = newn
        else:                               ##LL contains atleast one node
            temp = self.first
            while temp.next != None:
                temp = temp.next

            temp.next = newn

        self.iCount += 1

#####################################################################################################
    def Display(self):
        temp = self.first
        while (temp != None):
            print(f"|  {temp.data}  | -->", end ="  ")
            temp = temp.next

        print("NONE")

#################################################################################################

    def Count(self):
        return self.iCount
#################################################################################################

    def DeleteFirst(self):
        if (self.first == None):            ##LL is empty
            return
        else: 
            temp = self.first
            self.first = self.first.next
            del temp 

            self.iCount = self.iCount - 1  

#################################################################################################
    def DeleteLast(self):
        if (self.first == None):                                   ##LL is empty
            return
        elif (self.first.next == None):                            ##LL contains 1 node
            del self.first
            self.first = None
        else:                                                      ##LL contains more than 1 node
            temp = self.first
            while (temp.next.next != None):
                temp = temp.next
            del temp.next
            temp.next = None

        self.iCount = self.iCount - 1  

#################################################################################################
    def InsertAtPos(self, no, pos):
        if (pos < 1 or pos > (self.iCount +1)):
            print("invalid position")
            return
        
        if (pos == 1):
            self.InsertFirst(no)
        elif (pos == (self.iCount+1)):
            self.InsertLast(no)

        else:
            newn = Node(no)
            temp = self.first

            for i in range(1, pos-1, 1):
                temp = temp.next

            newn.next = temp.next
            temp.next = newn

            self.iCount = self.iCount + 1

        

#################################################################################################
def main():
    print("Demonstration of Linked List .")

    Sobj = SinglyLL()
    Sobj.InsertFirst(51)
    Sobj.InsertFirst(21)
    Sobj.InsertFirst(11)

    Sobj.InsertLast(101)
    Sobj.InsertLast(111)
    Sobj.InsertLast(121)

    
    Sobj.Display()

    

    iRet = Sobj.Count()
    print(f"number of nodes in linked list are : {iRet}")

    Sobj.InsertAtPos(105,5)
    Sobj.Display()
    iRet = Sobj.Count()
    print(f"number of nodes in linked list are : {iRet}")




#################################################################################################


if __name__ == "__main__":
    main()

#################################################################################################