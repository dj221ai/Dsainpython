def binSearch(arr, n):
    low,high=0,len(arr)-1
    # pos=-1
    while low<=high:
        mid=(low+high)//2
        if n==arr[mid]:
            # pos=mid
            return mid
        elif n>arr[mid]:
            low=mid+1
        else:
            high=mid-1
    
    return -1


print(binSearch(list(range(1,10001)), 12311))
