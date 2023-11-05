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

def atPos(head, pos, x):
    temp=Node(x)
    if pos==1:
        temp.next=head
        return temp
    
    currNode=head
    for _ in range(pos-2):
        currNode=currNode.next
        if currNode is None:
            return head

    temp.next=currNode.next
    currNode.next=temp
    return head

def deleteAtBeginning(head):
    return None if head is None else head.next

def deleteAtLast(head):
    if head is None:
        return None
    if head.next is None:
        return None
    currNode=head
    while currNode.next.next is not None:
        currNode=currNode.next
    
    currNode.next=None
    return head

# def deleteGivenPointer(pointer):
#     if 



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
head=insertAtStart(head, 13)
head=atPos(head, 3, 30)
head=atPos(head, 5, 41)
head=insertAtEnd(head, 14)
head=insertAtEnd(head, 78)
head=insertAtEnd(head, 22)


traverseAndPrint(head)
# print(search(head, 10))
print()
print("After deleting head ------------------")
print()
# print(deleteAtBeginning(head))
head=deleteAtBeginning(head)
traverseAndPrint(head)
print()
print("After deleting last ------------------")
print()
head=deleteAtLast(head)
traverseAndPrint(head)
print()
print("After deleting pointer position ------------------")
print()
# head=deleteGivenPointer(head, 4)
traverseAndPrint(head)
