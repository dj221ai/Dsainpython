def isSorted(lst):
    if len(lst)<=1:
        return True
    
    for i in range(1, len(lst)):
        if lst[i-1] > lst[i]:
            return False
    return True


if __name__=='__main__':
    lst=[]
    # lst=[3,1,5,9,561,2311, 561, 22]
    print(isSorted(lst))