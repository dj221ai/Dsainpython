#  T.C --> O(n)
def findAllDivisorsNaive(n:int):
    for i in range(1, n+1):
        if n%i==0:
            print(i)


if __name__=='__main__':
    n=int(input("Enter nos:"))
    findAllDivisorsNaive(n)


# T.C O(sqrt(n))
def findDivisorEfficientSorted(n:int):
    i=1
    while i**2<n:
        if n%i==0:
            print(i)
            # temp=n//i
            # print(temp)
        i+=1
    
    while i>=1:
        if n%i==0:
            print(n//i)
        i-=1


if __name__=='__main__':
    n=int(input("Enter nos:"))
    findDivisorEfficientSorted(n)



