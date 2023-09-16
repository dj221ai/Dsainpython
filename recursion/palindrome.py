def check_palindrome(str1,start=None,end=None):
    # reverse using iteration
    rev=''
    for i in str1:
        rev=i+rev

    print(rev)

    if rev==str1:
        print("yes")
    else:
        print("no")

    # return check_palindrome(n)
    # i=0
    # while i<len(n):
    #     print(n[i])
    #     i+=1

    # Print characters using recuring
    # if len(n)==0:
    #     return
    # # rev=n[0]+rev
    # # print(rev)
    # check_palindrome(n[1:])
    # print(n[0])







check_palindrome("abba")
