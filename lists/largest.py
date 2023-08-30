def findLargest(lst):
    if len(lst) < 1:
        return []
    x=lst[0]
    for i in lst:
        if i>x:
            x=i
    return x


if __name__=='__main__':
    lst=[10,20,30,90,4,5,7,36,1,11]
    # lst=[2]
    print(findLargest(lst))
