def findFirstOccurence(arr, ele):
    l,h=0,len(arr)-1
    res=-1

    while l<=h:
        mid=(l+h)//2
        if arr[mid] == ele:
            res=mid
            h=mid-1
        elif arr[mid] < ele:
            l=mid+1
        elif arr[mid] > ele:
            h=mid-1
        # else:
        #     if (mid==0 or arr[mid-1]!=arr[mid]):
        #         return mid
        #     else:
        #         h=mid-1
    return res


print(findFirstOccurence([1,10,10,10,20,20,40], 290))