# naive solution -- Time complexity is O(n)
def count_zeros(n):
    fact=1
    i=1
    if n==0:
        return 1
    while (i<=n):
        fact=fact*i
        i+=1
    
    print("facotiral is ", fact)

    count=0
    while(fact%10==0):
        count+=1
        fact=fact//10
        

    print("zeros are: ", count)

count_zeros(10)


# optimized solution 
def countZeros(n):
    i=5
    result=0
    while (i<=n):
        result=n//i + result
        i*=5
    return result

print(countZeros(1000))