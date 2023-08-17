# naive approach
def isPrime(n:int):
    return False if n==1 else all(n%i != 0 for i in range(2, n))

    # if n==1:
    #     return False
    # for i in range(2, n):
    #     if n%i==0:
    #         return False
    # return True

if __name__=='__main__':
    n=int(input("Enter nos: "))
    print(isPrime(n))
