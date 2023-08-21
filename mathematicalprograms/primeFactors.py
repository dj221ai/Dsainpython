def isprime(n:int):
    if n==1:
        return False
    elif n in {2,3}:
        return True
    elif n%2==0 or n%3==0:
        return False
    else:
        i=5
        while i**2<=n:
            if n%i==0 or n%(i+2)==0:
                return False
            i+=6
        return True

# naive approach
def primeFactors(n:int):
    for i in range(2, n):
        isPrime = isprime(i)
        if isPrime == True:
            temp=i
            while (n%temp==0):
                print(i)
                temp *= i

if __name__=='__main__':
    n=int(input("Enter nos: "))
    primeFactors(n)

