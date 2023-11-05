class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

def printList(head):
    if head is None:
        return None
    curr=head
    while curr is not None:
        print(curr.data)
        curr=curr.next

# Naive Approach
def lengthOfList(head):
    curr=head
    length=0

    while curr is not None:
        length+=1
        curr=curr.next

    return length

def middle(head):
    mid=lengthOfList(head)//2
    pos=1
    curr=head
    while pos!=(mid+1):
        curr=curr.next
        pos+=1

    return curr.data




head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=Node(50)
head.next.next.next.next.next=Node(60)

# print(lengthOfList(head))

print(middle(head))