def findOnes(arr):
    l,h=0,len(arr)-1
    first=0

    while l<=h:
        mid=(l+h)//2
        if arr[mid] == 1:
            first=mid
            h=mid-1
        elif arr[mid] < 1:
            l=mid+1
        elif arr[mid] > 1:
            h=mid-1

    return len(arr) - first if first >= 1 else first
    
print(findOnes([0,0,0,1,1,1,1,1]))


