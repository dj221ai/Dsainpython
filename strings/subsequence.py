# naive approach of finding all subsequence
# def findsubsequence():
    
#     s='ABCD'
#     l=[]
#     for i in range(len(s)):
#         l.append(s[i])

#     for i in range(len(s)):
#         for j in range(i+1, len(s)):
#             # print(s[i]+s[j])
#             if s[i]+s[j] not in l:
#                 l.append(s[i]+s[j])

    
#     for i in range(len(s)):
#         # print(s[i:])
#         if s[i:] not in l:
#             l.append(s[i:])

#     l.insert(0, '')
#     print(l)

# findsubsequence()

# efficient appraoch 1
# def isSubsequence(s1,s2):
#     i,j=0,0
#     while i<len(s1) and j<len(s2):
#         if s1[i]==s2[j]:
#             j+=1
#         i+=1

#     if j==len(s2):
#         return True
#     else:
#         return False


# s1='ABCD'
# s2='BA'
# print(isSubsequence(s1, s2))


# recursive appraoch 
def isSubsequence(s1,s2,m,n):
    if n==0:
        return True
    if m==0:
        return False
    if s1[m-1]==s2[n-1]:
        return isSubsequence(s1,s2, m-1, n-1)
    else:
        return isSubsequence(s1, s2, m-1, n)
    

s1='ABCD'
s2='BD'
print(isSubsequence(s1, s2, len(s1), len(s2)))