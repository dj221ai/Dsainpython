class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

def printList(head):
    if head is None:
        return None
    currNode=head
    while currNode is not None:
        print(currNode.data)
        currNode=currNode.next

def deleteWithPointer(node):
    print("delete pointer node")
    temp=node.next
    node.data=temp.data
    node.next=temp.next



# def insertAtOne(head)
head=Node(10)
head.next=Node(20)
head.next.next=Node(40)
head.next.next.next=Node(50)

# print(head.data, head.next.data, head.next.next.data, head.next.next.data, end=' ')
printList(head)
deleteWithPointer(40)

