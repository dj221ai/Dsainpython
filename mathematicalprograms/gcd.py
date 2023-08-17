# naive solution -- T.C. -- O(min(a,b))

# Euclidean mtd 1
# def find_gcd(a:int,b:int):
#     while (a!=b):
#         if (a>b):
#             a -= b
#         else:
#             b -= a
#     return a


# print(find_gcd(12,15))

# Euclidean mtd 2 
def find_gcd(a:int, b:int):
    if b==0:
        return a
    return find_gcd(b, a%b)

print(find_gcd(12,151))