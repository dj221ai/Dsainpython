def mergesubarrays(arr,l,mid,h):
    left=arr[l:mid+1]
    right=arr[mid+1:h+1]
    i,j,k=0,0,l

    # print(left,right)

    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1