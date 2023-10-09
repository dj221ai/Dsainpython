from mergesubarrays import mergesubarrays
import random

def divide(arr, l, h):
    if h>l:
        mid=l+(h-l)//2
        divide(arr, l, mid)
        divide(arr, mid+1, h)
        mergesubarrays(arr, l, mid, h)

    return arr


if __name__=='__main__':
    arr=random.sample(range(1, 1000), 25)
    print(arr)
    print()
    # arr=[23,15,93,19,6, 87]
    l,h=0,len(arr)-1
    print(divide(arr,l,h))