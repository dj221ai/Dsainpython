def reverselist(lst):
    s = 0
    e = len(lst) - 1

    while s < e:
        lst[s], lst[e] = lst[e], lst[s] # swapping left element to right and right element to left
        s += 1
        e = e - 1
    # return [lst[i-1] for i in range(len(lst), 0, -1)]


if __name__=='__main__':
    lst=[3,1,5,9,561,2311, 561, 22]
    print(reverselist(lst))

