def secondLargestEle(lst):
    if len(lst) <= 1:
        return None

    large=lst[0]
    sLarge=None

    for i in lst[1:]:
        # print(i)
        if i > large:
            # print(sLarge, large)
            sLarge=large
            large=i
        elif i!= large:
            if sLarge is None or sLarge<i:
                sLarge=i
    
    return sLarge



if __name__=='__main__':
    lst=[3,1,5,9,561,2311, 561, 22]
    # lst=[23]
    print(secondLargestEle(lst))

