# iterative approach
def find_facto():

    n=int(input("Enter nos: "))
    temp=1
    if n==0:
        print(f"factorial of {n} is 1")
    for i in range(1, n+1):
        temp=temp*i

    print(temp)

# find_facto()

# recursive approach
def recur_facto(n):
    if n==0:
        return 1
    return n*recur_facto(n-1)


if __name__=='__main__':
    nos=5
    print(recur_facto(nos))

