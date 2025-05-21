class SingleLinkedList:
    def __init__(self,value,nextNode=None):
        self.value = value
        self.nextNode = nextNode

snode1= SingleLinkedList("1")
snode2= SingleLinkedList("2")
snode3= SingleLinkedList("3")
snode4= SingleLinkedList("4")

snode1.nextNode= snode2
snode2.nextNode= snode3
snode3.nextNode= snode4

currentNode=snode1
while True:
    print(currentNode.value,">>>",end=" ")
    if currentNode.nextNode==None:
        print("None")
        break
    currentNode= currentNode.nextNode


