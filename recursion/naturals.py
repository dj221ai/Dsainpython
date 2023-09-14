def natural(n):
    if n==0:
        return 1
    natural(n-1)
    # print()
    print(n)
natural(41)
