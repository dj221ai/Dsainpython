class Node:
    def __init__(self, data):
        self.data=data
        self.next=None


def push(head, data):
    temp=Node(data)
    if head is None:
        return temp
    temp.next=head
    return temp
    
    

def pop(head):
    if head is None:
        return
    head=head.next
    return head

def peek(head):
    if head is None:
        return
    return head.data

def size(head):
    if head is None:
        return 0
    curr=head
    length=0
    while curr is not None:
        length+=1
        curr=curr.next

    return length

def isEmpty(head):
    return head is None

def printList(head):
    curr=head
    while curr is not None:
        print(curr.data, end=' ')
        curr=curr.next


head=None
head=push(head, 10)
head=push(head, 20)
head=push(head, 30)
print("PUSH==========================")
print(isEmpty(head))
print(size(head))
printList(head)
print()
print("PEEK==========================")
print(peek(head))
print(size(head))
# printList(head)
print()
print("POP==========================\n")
head=pop(head)
# head=pop(head)
# head=pop(head)
print(isEmpty(head))
print(size(head))
printList(head)
print()
print("PEEK==========================")
print(peek(head))
print(size(head))
