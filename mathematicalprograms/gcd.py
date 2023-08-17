# naive solution -- T.C. -- O(min(a,b))
def naive_gcd(a,b):
    res=a if a<b else b
    while(res>0):
        if (a%res==0 and b%res==0):
            break
        res-=1
    return res
print(naive_gcd(10, 15))

# Euclidean mtd 1
def find_gcd(a:int,b:int):
    while (a!=b):
        if (a>b):
            a -= b
        else:
            b -= a
    return a


print(find_gcd(12,15))

# Euclidean mtd 2 
def find_gcd(a:int, b:int):
    if b==0:
        return a
    return find_gcd(b, a%b)

print(find_gcd(12,151))