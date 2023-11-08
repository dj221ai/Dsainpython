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


# O(n) solution
def insertLinearMtd(head, x):
    temp=Node(x)
    if head is None:
        temp.next=temp
        return temp
    
    curr=head
    while curr.next is not head:
        curr=curr.next
    
    curr.next=temp
    temp.next=head
    return temp


def insertdirectMtd(head, x):
    temp=Node(x)
    if head is None:
        temp.next=temp
        return temp
    
    else:
        temp.next=head.next
        head.next=temp
        temp.data, head.data=head.data, temp.data
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
# head=insertLinearMtd(head, 15)
head=insertdirectMtd(head, 25)
head=insertdirectMtd(head, 251)
traverse(head)

