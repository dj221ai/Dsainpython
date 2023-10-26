def distinct(arr):
    res=0
    dictab={}
    for i in range(len(arr)):
        if arr[i] not in dictab:
            res+=1
        dictab[arr[i]]=arr[i]
    
    print(res)



arr=[10,20,10,30,30,20,11]
distinct(arr=arr)

