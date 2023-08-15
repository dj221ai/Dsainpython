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


    

find_lcm()