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

# Naive approach :- using length of list approach
def lengthOfList(head):
    curr=head
    length=0
    while curr is not None:
        length+=1
        curr=curr.next

    return length

def findNthNodeFromEndUsingLength(head, n):
    if n>lengthOfList(head):
        return "invlid length"
    curr=head
    i=1
    pos=lengthOfList(head)-n+1
    print("pos ", pos)
    while curr is not None:
        if i==pos:
            return curr.data
        curr=curr.next
        i+=1

# Using Two pointer approach
def findNthNodeFromEndUsingTwoPointers(head, n):
    if head is None:
        return
    
    first=head
    second=head

    for _ in range(1, n+1):
        if first is None:
            return "Invalid"
        first=first.next

    while first is not None:
        second=second.next
        first=first.next

    return second.data

    

    


head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=Node(50)
head.next.next.next.next.next=Node(60)
head.next.next.next.next.next.next=Node(70)

# printList(head)
n=5
# print(findNthNodeFromEndUsingLength(head, n))
print(findNthNodeFromEndUsingTwoPointers(head, n))

