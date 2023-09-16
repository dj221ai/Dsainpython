def sumofdigits(n):
    c=0
    # while n>0:
    #     rem=n%10
    #     c+=rem
    #     n//=10

    # print(c)

    return n if n<10 else sumofdigits(n//10) + n%10



print(sumofdigits(9))
