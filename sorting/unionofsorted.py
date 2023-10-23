def unionoftwosortedarr(a,b):
    m,n=len(a),len(b)
    i,j=0,0
    while i<m and j<n:
        if (i>0 and a[i]==a[i-1]):
            i+=1
        elif(j>0 and b[j]==b[j-1]):
            j+=1
        elif a[i]<b[j]:
            print(a[i], end=" ")
            i+=1
        elif a[i]>b[j]:
            print(b[j], end=" ")
            j+=1
        else:
            print(a[i], end=" ")
            i+=1
            j+=1

    while i<m:
        if i>0 and a[i]!=a[i-1]:
            print(a[i], end=" ")
        i+=1
    while j<n:
        if j>0 and b[j]!=b[j-1]:
            print(b[j], end=" ")
        j+=1


if __name__=='__main__':
    a=[3,5,8,8,9,9,9,9,9,9,18, 92,99,99,99,99,100,100,101]
    b=[2,8,9,10,15,35,42,67,67,88,91,95,96,100,100,101,102,102]
    unionoftwosortedarr(a,b)