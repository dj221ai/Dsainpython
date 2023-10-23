def countInversion(arr, l, h):
    getInv=0
    if l<h:
        mid=l+(h-l)//2
        getInv += countInversion(arr, l, mid)
        getInv += countInversion(arr, mid+1, h)
        getInv += findInversion(arr, l, mid, h)

    return getInv


def findInversion(arr, l, mid, h):
    a=arr[l:mid+1]
    b=arr[mid+1:h+1]
    i,j,k=0,0,l
    inv=0

    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            arr[k]=a[i]
            i+=1
        else:
            arr[k]=b[j]
            inv+=len(a)-i
            j+=1
        k+=1

    while i<len(a):
        arr[k]=a[i]
        i+=1
        k+=1
    while j<len(b):
        arr[k]=b[j]
        j+=1
        k+=1

    print(arr)
    return inv

if __name__=='__main__':
    # arr=random.sample(range(1, 1000), 25)
    # print(arr)
    # arr=[4,3,2,1,5]
    # arr=[10,5,30,15,7,8]
    arr=[2,4,1,3,5]
    l,h=0,len(arr)-1
    print(countInversion(arr,l,h))

