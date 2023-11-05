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

def sortedInsert(head, item):
    # print(head.data)
    temp=Node(item)
    if head is None:
        return temp
    elif item < head.data:
        temp.next=head
        return temp
    else:
        curr=head
        while curr.next != None and curr.next.data < item:
            curr=curr.next

        # temp=Node(item)
        temp.next=curr.next
        curr.next=temp
        return head

    
    

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=Node(50)
# head=None

printList(head)

print("=================")

sortedInsert(head, 56)
printList(head)
print("=================")

sortedInsert(head, 2)
printList(head)
