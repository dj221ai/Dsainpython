def findOnes(arr):
    l,h=0,len(arr)-1
    first=0
    last=-1

    # while l<=h:
    #     mid=(l+h)//2
    #     if arr[mid] == 1:
    #         first=mid
    #         h=mid-1
    #     elif arr[mid] < 1:
    #         l=mid+1
    #     elif arr[mid] > 1:
    #         h=mid-1


    while l<=h:
        mid=(l+h)//2
        if arr[mid] == 1:
            last=mid
            l=mid+1
            print("last is ", last)
            # return mid
        elif arr[mid] < 1:
            h=mid-1
        elif arr[mid] > 1:
            l=mid+1

    # return len(arr) - first if first >= 1 else first
    print("Laast is ", last)

    return last+1 if last>=0 else 0
    
# print(findOnes([0,0,0,1,1,1,1,1,1]))
# print(findOnes([20,18,17,14,13,11,10,8,9,4], 11))
print(findOnes([1,0,0,0,0]))


