def intersectionofTwoSortedarray(a,b):
    i,j,m,n=0,0,len(a),len(b)

    while i<m and j<n:
        if (i>0 and a[i-1]==a[i]):
            i+=1
        elif (j>0 and b[j-1]==b[j]):
            j+=1
        elif a[i]==b[j]:
            print(a[i], end=" ")
            i+=1
            j+=1
        elif a[i]<b[j]:
            i+=1
        elif a[i]>b[j]:
            j+=1
        


if __name__=='__main__':
    a=[1,20,20,40,60]
    b=[2,20,20,20]
    # a=[3,5,10,10,10,15,25,20]
    # b=[5,10,10,15,30]
    intersectionofTwoSortedarray(a,b)