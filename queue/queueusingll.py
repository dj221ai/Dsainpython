class Node:
    def __init__(self, data):
        self.data=data
        self.next=None


class MyQueue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0

    def length(self):
        return self.size
    
    def isEmpty(self):
        return self.size==0
    
    def getFront(self):
        return self.front.data
    
    def getRear(self):
        return self.rear.data
    
    def enqueue(self, x):
        temp=Node(x)
        if self.rear is None:
            self.front=temp
        else:
            self.rear.next=temp
        self.rear=temp
        self.size+=1

    def dequeue(self):
        if self.front is None:
            return None
        else:
            res=self.front.data
            self.front=self.front.next
            if self.front is None:
                self.rear = None
            self.size-=1
            return res
        
    def printQueue(self):
        # print(self.front.data, self.rear.data)
        curr=self.front
        while curr is not None:
            print(curr.data, end=' ')
            curr=curr.next
        

q=MyQueue()
q.enqueue(23)
q.enqueue(34)
q.enqueue(12)
q.printQueue()
print()
print(q.getFront())
print(q.getRear())
print()
print(q.dequeue())
q.printQueue()

    