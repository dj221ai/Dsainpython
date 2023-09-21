def findLast(arr, n):
    l,h=0,len(arr)-1
    res=-1
    while l<=h:
        mid=(l+h)//2
        if arr[mid] == n:
            res=mid
            l=mid+1
        elif arr[mid] > n:
            h=mid-1
        else:
            l=mid+1

    return res


print(findLast([4,10,10,10,20,20,20,20,40,40], 10))