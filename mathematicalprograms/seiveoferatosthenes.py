# It is used for finding prime numbers upto certain number

# Efficient Mtd 1
def sieve(n):

    if n<=1:
        return
    
    primes=[True]*(n+1)
    # print(primes)
    i=2
    while i**2<=n:
        if primes[i]:
            for j in range(2*i, n+1, i):
                primes[j] = False
        i+=1

    for i in range(2, n+1):
        if primes[i]:
            print(i, end=' ')


    print()


if __name__=='__main__':
    n=int(input("Enter nos: "))
    sieve(n)

# More optimised mtd
def sieveOptimisedMtd(n:int):
    if n<=1:
        return
    primes=list(range(n+1))
    # print(primes)
    primes[0]=0
    primes[1]=0
    # print(primes)
    
    i=2
    while i**2<=n:
        if primes[i]:
            for j in range(i**2, n+1, i):
                primes[j] = 0
        
        i+=1

    # print(primes)

    for k in range(2, n+1):
        if primes[k]:
            print(k, end=' ')


    print()


if __name__=='__main__':
    n=int(input("Enter nos: "))
    sieveOptimisedMtd(n)
