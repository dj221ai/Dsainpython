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


# head=None

# head=Node(10)
# head.next=head

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=head

traverse(head)

