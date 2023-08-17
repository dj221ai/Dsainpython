# naive solution -- T.C. -- O(min(a,b))
def find_gcd(a:int,b:int):
    while (a!=b):
        if (a>b):
            a -= b
        else:
            b -= a
    return a


print(find_gcd(12,15))