class Node:
    def __init__(self, data):
        self.data=data
        self.next=None


def traverse(head):
    if head is None:
        return None
    print(head.data, end=' ')
    curr=head.next
    while curr is not head:
        print(curr.data, end=' ')
        curr=curr.next

# O(n)
def deleteAtHeadLinear(head):
    if head is None or head.next is head:
        return None
    curr=head
    while curr.next is not head:
        curr=curr.next
    curr.next=head.next
    return curr.next


# O(1)
def delHeadDirect(head):
    if head is None or head.next is head:
        return None
    # else:
    head.data=head.next.data
    head.next=head.next.next
    return head



# head=None

# head=Node(10)
# head.next=head

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=head

# traverse(head)
# head=deleteAtHeadLinear(head)
head=delHeadDirect(head)
traverse(head)