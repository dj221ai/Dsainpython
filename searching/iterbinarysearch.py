def binSearch(arr, n):
    low,high=0,len(arr) 
    # pos=-1
    while low<high:
        mid=(low+high)//2
        if n==arr[mid]:
            # pos=mid
            return mid
        elif n>arr[mid]:
            low=mid+1
        else:
            high=mid-1
    
    return -1


print(binSearch([10,23,29,34,45,67], 23))
