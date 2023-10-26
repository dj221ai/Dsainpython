# open addressing using linear probing
class Myhash:
    def __init__(self, capacity):
        self.capacity=capacity
        self.table=[-1]*capacity
        self.size=0

    def hash(self, x):
         return x%self.capacity
    
    
    def insert(self, ele):
        if self.size==self.capacity:
            return False
        
        if self.search(ele) == True:
            return False
        i=self.hash(ele)
        t=self.table
        while t[i] not in [-1,-2]:
            i=(i+1)%self.capacity
        t[i]=ele
        self.size+=1
        return True




    def search(self, ele):
        h=self.hash(ele)
        t=self.table
        i=h
        while t[i] !=-1:
            if t[i] == ele:
                return True
            i=(i+1)%self.capacity
            if i==h:
                return False
            
        return False
    
    def delete(self, ele):
        h=self.hash(ele)
        t=self.table
        i=h
        while t[i] !=-1:
            if t[i] == ele:
                t[i] = -2
                return True
            i=(i+1)%self.capacity
            if i==h:
                return False
        return False


            

    

        





mh=Myhash(10)
# print(mh.table)
mh.insert(49)
mh.insert(50)
mh.insert(54)
mh.insert(56)
mh.insert(58)
mh.insert(59)
mh.insert(63)
mh.insert(633)

print(mh.table)

mh.search(49)
mh.search(65)
mh.search(633)

print(mh.table)

mh.delete(49)

print(mh.table)
mh.delete(59)
print(mh.table)
