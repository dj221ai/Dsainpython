def palindrome():
    #  string mtd for palindrome
    # n=int(input("Enter nos : "))
    # n=str(n)
    # orig=''
    # rev=''
    # for i in n:
    #     orig=orig+i
    #     rev=i+rev

    # print(orig, rev)
    # if orig==rev:
    #     print("palindrome")
    # else:
    #     print("Not a palindrome!!")


    # digit mtd

    n=int(input("Enter nos: "))
    n1=n
    reverse_nos = 0
    # print(n//10)
    while n>0:
        remainder = n%10
        reverse_nos = (reverse_nos*10) + remainder
        n//=10

    if reverse_nos==n1:
        print("Palindrome Number")
    else:
        print("Not a Palindrome Number")



palindrome()