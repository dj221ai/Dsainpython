# Naive o(n**2)
# def leftmost(s):
#     for i in range(len(s)):
#         for j in range(i+1, len(s)):
#             if s[i]==s[j]:
#                 return i

#     return -1


# better approach o(n)
# def leftmost(s):
#     count=[0]*256
#     for i in range(len(s)):
#         count[ord(s[i])]+=1

#     for j in range(len(s)):
#         if count[ord(s[j])] > 1:
#             return j
        
#     return -1

# efficient 1
# import sys
# CHAR=256
# def leftmost(s):
#     fIndex=[-1]*CHAR
#     res=sys.maxsize
#     for i in range(len(s)):
#         if fIndex[ord(s[i])]==-1:
#             fIndex[ord(s[i])]=i
#         else:
#             res=min(res, fIndex[ord(s[i])])

#     if res==sys.maxsize:
#         return -1
#     else:
#         return res
    

# efficient 2
def leftmost(s):
    visited=[False]*256
    res=-1

    for i in range(len(s)-1,-1,-1):
        if visited[ord(s[i])]==True:
            res=i
        else:
            visited[ord(s[i])]=True

    return res


print(leftmost('abccdec'))
