class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

def printList(head):
    if head is None:
        return None
    curr=head
    while curr is not None:
        print(curr.data, end=' ')
        curr=curr.next

def recursiveMtdOne(head):
    if head is None or head.next is None:
        return head
    newhead=recursiveMtdOne(head.next)
    head.next.next=head
    head.next=None
    print(newhead.data)
    return newhead


def recursiveMtdTwo(head, prev=None):
    if head is None:
        return prev
    curr=head
    temp=curr.next
    curr.next=prev
    return recursiveMtdTwo(temp, curr)

    


# head=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=Node(50)

# printList(head)
# head=recursiveMtdOne(head)
head=recursiveMtdTwo(head)
print()
print("After Reversal =============== ")
printList(head)