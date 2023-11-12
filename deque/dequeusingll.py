class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.previous=None


class MyDeque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.length=0

    def size(self):
        return self.size
    
    def isEmpty(self):
        return self.size==0
    
    def insertRear(self, x):
        temp=Node(x)
        if self.rear is None:
            self.front=temp
        else:
            self.rear.next=temp
            temp.previous=self.rear
        self.rear=temp
        self.length+=1

    def deleteFront(self):
        if self.front is None:
            return None
        else:
            res=self.front.data
            self.front=self.front.next
            if self.front is None:
                self.rear=None
            else:
                self.front.previous=None
        self.length-=1
        return res
    
    def printDeque(self):
        curr=self.front
        while curr is not None:
            print(curr.data, end=' ')
            curr=curr.next
    


d=MyDeque()
d.insertRear(12)
d.insertRear(11)
d.insertRear(10)
d.printDeque()
print()
print()
print(d.deleteFront())
d.printDeque()

