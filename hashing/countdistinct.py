def distinct(arr):
    res=0
    dictab={}
    for i in range(len(arr)):
        if arr[i] not in dictab:
            res+=1
        dictab[arr[i]]=arr[i]
    
    print(res)



def TwoSum(arr):
    dic={}
    res=0
    for i in range(len(arr)):
        if arr[i] not in dic:
            dic[arr[i]] = 0
        dic[arr[i]]+=1

    for k,v in dic.items():
        if v==1:
            res+=1

    
    print(dic)
    print(res)




# arr=[10,20,10,30,30,20,11]
# distinct(arr=arr)]

arr=[10,20,30,40,50,10,60,80,70]
print(TwoSum(arr))

