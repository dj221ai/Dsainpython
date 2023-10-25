#  left rotate by one
def left_shift(lst):
    x=lst[0]
    for i in range(1, len(lst)):
        lst[i-1]=lst[i]

    lst[len(lst)-1]=x

    return lst



if __name__=='__main__':
    lst=[10,20,30,40]
    print(left_shift(lst))

# Right Rotate Array by k

def rotate(arr,k):
    k=k%len(arr)
    s,e=0,len(arr)-1

    while s<e:
        arr[s],arr[e]=arr[e],arr[s]
        s+=1
        e-=1

    s,e=0,k-1
    print(e,k)
    while s<e:
        print(s, arr[s])
        print(e, arr[e])
        arr[s],arr[e]=arr[e],arr[s]
        s+=1
        e-=1
    s,e=k,len(arr)-1
    print(e,k)
    while s<e:
        print(s, arr[s])
        print(e, arr[e])
        arr[s],arr[e]=arr[e],arr[s]
        s+=1
        e-=1

    return arr

# left rotate array by k places

def leftrotate(arr,k):
    k=k%len(arr)
    s,e=0,k-1
    while s<=e:
        arr[s],arr[e]=arr[e],arr[s]
        s+=1
        e-=1

    s,e=k,len(arr)-1
    while s<=e:
        arr[s],arr[e]=arr[e],arr[s]
        s+=1
        e-=1
    s,e=0,len(arr)-1
    while s<=e:
        arr[s],arr[e]=arr[e],arr[s]
        s+=1
        e-=1

    return arr

# arr = "hellosir"
arr = [1,2,3,4,5]
k=2
leftrotate(arr,k)
# rotate(arr,k)
print(*arr)
