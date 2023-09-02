def left_shift(lst):
    x=lst[0]
    for i in range(1, len(lst)):
        lst[i-1]=lst[i]

    lst[len(lst)-1]=x

    return lst



if __name__=='__main__':
    lst=[10,20,30,40]
    print(left_shift(lst))
