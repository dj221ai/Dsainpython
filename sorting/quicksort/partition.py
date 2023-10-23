def partitionAtgivenIndexNaive():
    l=[3,8,6,12,10,7]
    n=len(l)
    p=5
    # l1=[l[p]]
    # print(l1)

    # for item in l:
    #     if item < l[p]:
    #         l1 = [item] + l1
    #     elif item == l[p]:
    #         continue
    #     else:
    #         l1.append(item)

    # print(l1)
    l[p],l[n-1]=l[n-1],l[p]
    print(l)
    temp = [i for i in l if i<=l[n-1]]
    # print(temp)

    for i in l:
        if i>l[n-1]:
            temp.append(i)

    # print(temp)

    for i in range(len(l)):
        l[i]=temp[i]

    print(l)




partitionAtgivenIndexNaive()