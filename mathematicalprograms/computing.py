def findPowerValues(n,x):

    res=1
    for _ in range(n):
        res=res*x

    print(res)





if __name__=='__main__':
    n,x=map(int, input("Enter values: ").split())
    findPowerValues(n,x)



def power(x,n):
    # if n%2==0:
    #     return pow(x,n//2)*pow(x, n//2)
    # else:
    #     return pow(x, n-1)*x

    if n==0:
        return 1
    temp = power(x, n//2)
    temp*=temp
    return temp if n%2==0 else temp*x




if __name__=='__main__':
    x,n=map(int, input("Enter values: ").split())
    print(power(x, n))
