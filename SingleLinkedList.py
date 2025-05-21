# class SingleLinkedList:
#     def __init__(self,value,nextNode=None):
#         self.value = value
#         self.nextNode = nextNode

# snode1= SingleLinkedList("1")
# snode2= SingleLinkedList("2")
# snode3= SingleLinkedList("3")
# snode4= SingleLinkedList("4")

# snode1.nextNode= snode2
# snode2.nextNode= snode3
# snode3.nextNode= snode4

# currentNode=snode1
# while True:
#     print(currentNode.value,">>>",end=" ")
#     if currentNode.nextNode==None:
#         print("None")
#         break
#     currentNode= currentNode.nextNode
class Node:
    def __init__(self,data):
        self.data = data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def InsertAtTheBeginning(self,new_data):
        new_node= Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def InsertAtTheEnd(self,new_data):
        new_node= Node(new_data)
        if self.head==None:
            self.head=new_node
            return
        last= self.head
        while last.next:
            last= last.next
        last.next=new_node
    def deleteFromBeginning(self):
        if self.head==None:
            return
        temp= self.head
        self.head= self.head.next
        temp=None
    def deleteFromEnd(self):
        if self.head==None:
            return "List is Empty"
        if self.head.next==None:
            self.head=None
            return
        second_last= self.head
        while second_last.next.next:
            second_last= second_last.next
        second_last.next=None

    def printLinkedList(self):
        temp= self.head
        while temp:
            print(temp.data)
            temp= temp.next
        print()

if __name__=="__main__":
    llist= LinkedList()
    llist.InsertAtTheBeginning("fox")
    llist.InsertAtTheBeginning("brown")
    llist.InsertAtTheBeginning("quick")
    llist.InsertAtTheBeginning("the")
    llist.printLinkedList()
    llist.InsertAtTheEnd("jumps")
    llist.printLinkedList()
    llist.deleteFromEnd()
    llist.deleteFromBeginning()
    llist.InsertAtTheBeginning("a")
    llist.printLinkedList()


