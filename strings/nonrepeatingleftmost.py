def leftmostNonRepeating(s):
    visited=[0]*256

    for i in range(len(s)):
        visited[ord(s[i])]+=1

    for j in range(len(s)):
        if visited[ord(s[j])] == 1:
            return j
    else:
        return -1



print(leftmostNonRepeating("abcabcd"))