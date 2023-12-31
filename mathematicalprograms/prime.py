# naive approach
def isPrimeNaive(n:int):
    return False if n==1 else all(n%i != 0 for i in range(2, n))

    # if n==1:
    #     return False
    # for i in range(2, n):
    #     if n%i==0:
    #         return False
    # return True

if __name__=='__main__':
    n=int(input("Enter nos: "))
    print(isPrimeNaive(n))


# Efficient Mtd1

def isPrimeMtdOne(n:int):
    if n==1:
        return False
    i=2
    while (i**2 <= n):
        if n%i==0:
            return False
        i+=1
    return True


if __name__=='__main__':
    n=int(input("Enter nos: "))
    print(isPrimeMtdOne(n))

# Efficient Mtd 2
def isPrimeMtdTwo(n:int):
    if n==1:
        return False
    # n==2 or n==3
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

if __name__=='__main__':
    n=int(input("Enter nos: "))
    print(isPrimeMtdTwo(n))
