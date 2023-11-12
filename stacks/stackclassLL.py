import math

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class MyStack:
    def __init__(self):
        self.head=None
        self.size=0

    def push(self, x):
        temp=Node(x)
        temp.next=self.head
        self.head=temp
        self.size+=1

    def length(self):
        return self.size
    
    def pop(self):
        if self.head is None:
            return math.inf
        res=self.head.data
        self.head=self.head.next
        self.size-=1
        return res
    
    def peek(self):
        if self.head is None:
            return math.inf
        return self.head.data
    
    def printList(self):
        if self.head is None:
            print(math.inf)
        curr=self.head
        while curr is not None:
            print(curr.data, end=' ')
            curr=curr.next


    
s=MyStack()
s.push(10)
s.push(20)
s.push(30)
print(s.length())
s.printList()
print()
s.pop()
s.pop()
s.pop()
s.printList()
print()
# print(s.peek())
s.printList()


