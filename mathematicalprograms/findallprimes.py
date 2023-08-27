def isPrime(n:int):
    if n==1:
        return False
    if n in {2,3}:
        return True
    elif n%2==0 or n%3==0:
        return False
    else:
        i=5
        while i**2<=n:
            if n%i==0 or n%(i+2) == 0:
                return False
            i+=6
        return True
    

def findPrimes(n:int):
    for i in range(2, n+1):
        if isPrime(i):
            print(i)

if __name__=='__main__':
    nos = int(input("Enter nos: "))
    findPrimes(nos)

