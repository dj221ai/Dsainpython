class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.previous=None


def printList(head):
    if head is None:
        return None
    curr=head
    while curr is not None:
        print(curr.data)
        curr=curr.next


def insertAtHead(head, x):
    temp=Node(x)
    if head is None:
        return temp
    temp.next=head
    head.previous=temp
    return temp

def insertAtEnd(head, x):
    temp=Node(x)
    if head is None:
        return temp
    curr=head
    while curr.next is not None:
        curr=curr.next
    temp.previous=curr
    curr.next=temp
    return head

def delHead(head):
    if head is None or head.next is None:
        return None
    head=head.next
    head.previous=None
    return head

def delEnd(head):
    if head is None or head.next is None:
        return None
    curr=head
    while curr.next.next is not None:
        curr=curr.next
    curr.next=curr.next.next
    return head
    


head=None

# head=Node(10)
# temp1=Node(20)
# temp2=Node(30)
# temp3=Node(40)
# head.next=temp1
# temp1.previous=head
# temp1.next=temp2
# temp2.previous=temp1
# temp2.next=temp3
# temp3.previous=temp2

head=insertAtHead(head, 23)
head=insertAtHead(head, 34)
head=insertAtEnd(head, 22)
head=insertAtEnd(head, 45)
printList(head)
print()
head=delHead(head)
# head=delHead(head)
# head=delHead(head)
printList(head)
print()
head=delEnd(head)
printList(head)

