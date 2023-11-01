def palindrome(s1):
    l,r=0, len(s1)-1
    while l<=r:
        if s1[l]!=s1[r]:
            return False
        l+=1
        r-=1

    return True

print(palindrome('abccba'))