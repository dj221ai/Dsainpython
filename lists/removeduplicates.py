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
