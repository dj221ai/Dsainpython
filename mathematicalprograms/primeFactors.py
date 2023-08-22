import math


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

# Efficient MTd1
def primeFactorsEfficientMtd(n:int):
    if n<=1:
        return False
    i=2
    while(i**2<=n):
        if isprime(i) == True:
            while(n%i==0):
                print(i)
                n//=i
        i+=1
    if n>1:
        print(n)

if __name__=='__main__':
    n=int(input("Enter nos: "))
    primeFactorsEfficientMtd(n)



# Efficient Mtd 2
def primeFactorsEfficientMtd2(n:int):
    # Print the number of two's that divide n
    while n % 2 == 0:
        print(2)
        n //= 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):

        # while i divides n , print i ad divide n
        while n % i== 0:
            print(i)
            n //= i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print(n)


if __name__=='__main__':
    n=int(input("Enter nos: "))
    primeFactorsEfficientMtd2(n)

