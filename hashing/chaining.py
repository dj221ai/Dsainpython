class MyHash:
    def __init__(self, b):
        self.BUCKET=b
        self.table = [[] for _ in range(b)]

    def insert(self, x):
        i=x%self.BUCKET
        self.table[i].append(x)

    def search(self, x):
        i=x%self.BUCKET
        return x in self.table[i]
    
    def removeEle(self, x):
        i=x%self.BUCKET
        if x in self.table[i]:
            self.table[i].remove(x)



mhash=MyHash(7)
mhash.insert(12)
mhash.insert(49)
mhash.insert(56)
mhash.insert(61)
mhash.insert(6)
mhash.insert(10)

print(mhash.table)
# mhash.search(10)
# mhash.search(33)
print(mhash.search(10))
print(mhash.search(33))

mhash.removeEle(12)
print(mhash.table)

