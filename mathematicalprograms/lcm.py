# naive approach T.C. O(a*b-max(a,b))
def find_lcm():
    n1=int(input("Enter 1st number: "))
    n2=int(input("Enter 2nd number: "))

    # naive solution -- # Time Complexity is O(n1*n2 - max(n1,n2))
    greater_nos = 0
    if n1>n2:
        greater_nos=n1
    else:
        greater_nos=n2

    while True:
        if greater_nos%n1==0 and greater_nos%n2==0:
            print(greater_nos)
            break
        greater_nos+=1


    

# find_lcm() -- # T.C. is o(log min(a,b))
def efficient_gcd(a,b):
    return a if b==0 else efficient_gcd(b, a%b)

def efficient_lcm(a,b):
    return (a*b)//efficient_gcd(a,b)

if __name__=='__main__':

    n1=int(input("Enter 1st number: "))
    n2=int(input("Enter 2nd number: "))
    print(efficient_lcm(n1,n2))




