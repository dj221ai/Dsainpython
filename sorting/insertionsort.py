import random
def insertionSorting(l):
    n=len(l)
    for i in range(1, n):
        temp=l[i]
        j=i-1
        while j>=0 and l[j]>temp:
                l[j+1] = l[j]
                j-=1
        l[j+1] = temp

    print(l)




# l=[10,5,8,20,2,18,20, 5,3,5]
l=random.sample(range(1, 1000), 25)
print(l)
print()

insertionSorting(l)
