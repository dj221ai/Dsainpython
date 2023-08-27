def findPowerValues(n,x):

    res=1
    for _ in range(n):
        res=res*x

    print(res)





if __name__=='__main__':
    n,x=map(int, input("Enter values: ").split())
    findPowerValues(n,x)