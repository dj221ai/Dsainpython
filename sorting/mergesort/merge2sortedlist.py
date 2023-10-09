def mergeTwoSortedList():
    a=[4,6,7,9]
    b=[1,3,5,23]
    c=[]
    m,n=len(a), len(b)
    i,j=0,0

    while i<m and j<n:
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1

    while i<m:
        c.append(a[i])
        i+=1
    while j<n:
        c.append(b[j])
        j+=1

    print(c)



mergeTwoSortedList()