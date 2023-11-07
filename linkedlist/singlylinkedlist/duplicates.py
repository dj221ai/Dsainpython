class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

def printList(head):
    if head is None:
        return "Empty"
    curr=head
    while curr is not None:
        print(curr.data)
        curr=curr.next

def removeDuplicates(head):
    if head is None:
        return None
    curr = head
    while curr is not None and curr.next is not None:
        if curr.data==curr.next.data:
            curr.next=curr.next.next
        else:
            curr=curr.next




head=Node(10)
head.next=Node(20)
head.next.next=Node(20)
head.next.next.next=Node(20)
head.next.next.next.next=Node(20)
head.next.next.next.next.next=Node(20)
head.next.next.next.next.next.next=Node(50)

removeDuplicates(head)
printList(head)