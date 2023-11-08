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

def delKthNode(head, k):
    if head is None:
        return None
    elif k==1:
        head.data=head.next.data
        head.next=head.next.next
        return head
    else:
        curr=head
        for _ in range(k-2):
            if curr is head:
                return head
            curr=curr.next
        # print(curr.data)
        curr.next=curr.next.next
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
head=delKthNode(head, 2)
traverse(head)
