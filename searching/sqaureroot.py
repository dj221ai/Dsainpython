def findSquareRoot(n):
    # Naive approach
    # i=1
    # while i**2<=n:
    #     i+=1

    # return i-1

    # Efficient Approach
    low,high=1,n
    ans=-1
    while low<=high:
        mid=(low+high)//2
        midSquare=mid**2
        if midSquare==n:
            return mid
        elif midSquare > n:
            high=mid-1
        else:
            low=mid+1
            ans=mid

    return ans



print(findSquareRoot(23))