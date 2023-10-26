def frequecyCounter(arr, n):
    c={}
    for i in range(n):
        if arr[i] not in c:
            c[arr[i]]=0
        c[arr[i]]+=1

    print(c)

    for k, v in c.items():
        print(k, v)


arr=[10,12,10,15,10,20,12,12,22,24,24,24,24,24,24,30]
print(arr)
n=len(arr)
frequecyCounter(arr, n)