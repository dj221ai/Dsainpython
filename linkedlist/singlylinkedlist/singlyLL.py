class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

def search(head, x):
    curr=head
    pos=1
    while curr is not None:
        if curr.data==x:
            return pos
        pos+=1
        curr=curr.next

    return -1

def insertAtStart(head, x):
    temp=Node(x)
    temp.next=head
    return temp

def insertAtEnd(head, x):
    if head is None:
        return Node(x)
    currNode=head
    while currNode.next != None:
        currNode=currNode.next

    currNode.next=Node(x)
    return head



def traverseAndPrint(head):
    currNode=head
    while currNode is not None:
        print(currNode.data)
        currNode=currNode.next

    










# head=Node(10)
# head.next=Node(20)
# head.next.next=Node(30)
head=None
head=insertAtStart(head, 23)
head=insertAtStart(head, 10)
head=insertAtStart(head, 33)
head=insertAtEnd(head, 14)
head=insertAtEnd(head, 78)
head=insertAtEnd(head, 22)

traverseAndPrint(head)
# print(search(head, 10))
