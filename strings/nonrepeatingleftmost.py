# def leftmostNonRepeating(s):
#     visited=[0]*256

#     for i in range(len(s)):
#         visited[ord(s[i])]+=1

#     for j in range(len(s)):
#         if visited[ord(s[j])] == 1:
#             return j
#     else:
#         return -1
    

# efficient 1
import sys
CHAR=256
def leftmostNonRepeating(s):
    fIndex=[-1]*CHAR
    for i in range(len(s)):
        if fIndex[ord(s[i])]==-1:
            fIndex[ord(s[i])]=i
        else:
            fIndex[ord(s[i])]=-2


    res=sys.maxsize
    for i in range(CHAR):
        if fIndex[i] >=0:
            res=min(res, fIndex[i])

    if res==sys.maxsize:
        return -1
    else:
        return res



print(leftmostNonRepeating("geeksforgeeks"))