def bubbleSort(lst):
    for i in range(len(lst)-1):
        swapped=False
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
                swapped=True
        if swapped==False:
            return

    return lst


print(bubbleSort([9,10,57,4,44,33,2,1]))