def removeDuplicates(lst):
    # using new list
    l1=[]
    for i in lst:
        if i not in l1:
            l1.append(i)

    return l1




if __name__=='__main__':
    lst = [10,20,20,30,30,30,30,40,5]
    print(removeDuplicates(lst))

# print("without using new list")

# without using new list returning new size

def removeWithoutNewListNaive(lst):
    res=1
    for i in range(1, len(lst)):
        if lst[res-1] != lst[i]:
            lst[res]=lst[i]
            res+=1

    return res



if __name__=='__main__':
    lst = [10,20,30,30,30,30,80,80]
    print(removeWithoutNewListNaive(lst))
