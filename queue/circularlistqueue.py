class CirluarList:
    def __init__(self, capacity):
        self.capacity=capacity
        self.queue=[None]*capacity
        self.size=0
        self.front=0

    def enque(self, item):
        if self.size==self.capacity:
            return None
        # else:
        rear=(self.front+self.size-1)%self.capacity
        rear=(rear+1)%self.capacity
        self.queue[rear]=item
        self.size+=1

    def dequeue(self):
        if self.size==0:
            return None
        # else:
        res=self.queue[self.front]
        self.front=(self.front+1)%self.capacity
        self.size-=1
        return res
        
    def getFront(self):
        return None if self.size==0 else self.queue[self.front]
    
    def getRear(self):
        if self.size==0:
            return None
        rear=(self.front+self.size-1)%self.capacity
        return self.queue[rear]
        

# rear=(front+size-1)%capcity
# enque-> rear=(rear+1)%capP
# deque-> front=(front+1)%cap

cl=CirluarList(10)
cl.enque(1)
cl.enque(2)
cl.enque(3)
cl.enque(4)
cl.enque(5)
cl.enque(6)
cl.enque(7)
cl.enque(8)
print(cl.queue, cl.size, cl.capacity, cl.getRear(), cl.getFront())
# cl.dequeue()
cl.enque(9)
# cl.dequeue()
# cl.dequeue()
# cl.dequeue()
cl.enque(91)
cl.dequeue()
cl.dequeue()
cl.enque(913)
print(cl.queue, cl.size, cl.capacity, cl.getRear(), cl.getFront())
