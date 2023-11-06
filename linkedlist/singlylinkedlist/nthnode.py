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

    # return curr.data
    

    


head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=Node(50)

# printList(head)
n=1
print(findNthNodeFromEnd(head, n))

