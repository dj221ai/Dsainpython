def countZeros(n):
    i=5
    sum1=0
    while (i<=n):
        sum1=n//i + sum1
        i*=5
    return sum1

print(countZeros(1000))