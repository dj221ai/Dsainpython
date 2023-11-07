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

def reverseWithoutUsingList(head):
    if head is None:
        return None
    if head.next is None:
        return head.data
    curr=head
    previous=None
    while curr is not None:
        nextVal=curr.next
        curr.next=previous
        previous=curr
        curr=nextVal

    return previous

        
    


# head=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=Node(50)

head=reverseWithoutUsingList(head)
printList(head)