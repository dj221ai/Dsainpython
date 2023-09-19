def recursiveBS(arr, n, low, high):
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]==n:
        return mid
    elif arr[mid] > n:
        return recursiveBS(arr,n,low,mid-1)
    else:
        return recursiveBS(arr,n,mid+1,high)
    


def bSearchMain(l, x):
    return recursiveBS(l, x, 0, len(l) - 1)


l = list(range(1,500))
# l = [10, 20, 30, 40, 50, 60]
print(bSearchMain(l, 301))
print(bSearchMain(l, 601))


