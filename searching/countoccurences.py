def findFirstOccurence(arr, x):
    first=-1
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            first=mid
            high=mid-1
        elif arr[mid] < x:
            low=mid+1
        else:
            high=mid-1
    
    return first


def findLastOccurence(arr, x):
    last=-1
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            last=mid
            low=mid+1
        elif arr[mid] < x:
            low=mid+1
        else:
            high=mid-1
    
    return last



def countOccurrence(arr, x):
    firstVal = findFirstOccurence(arr, x)

    if firstVal == -1:
        return 0

    lastVal = findLastOccurence(arr, x)

    return lastVal-firstVal+1


if __name__=='__main__':
    nos=int((input("Enter nos to find total count: ")))
    print(countOccurrence([1,4,4,5,5,5,5,5,5,5,5,5,17,28,90], nos))