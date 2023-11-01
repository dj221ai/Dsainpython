# with count() in linear time
# def anagram(s1,s2):
#     flag=0
#     if len(s1)!=len(s2):
#         return False
#     d={}
#     for i in s1:
#         if i not in d:
#             d[i]=0
#         d[i]+=1

#     for j in s2:
#         flag = 1 if j in d and s2.count(j) == d[j] else 0

#     return flag == 1


#  without using inbuilt count
def anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    
    count = [0]*256
    for i in range(len(s1)):
        count[ord(s1[i])]+=1
        count[ord(s2[i])]-=1

    for x in count:
        if x!=0:
            return False
    
    return True


s1,s2 ='abx', 'xba'
print(anagram(s1,s2))