# naive solution using stack/list with O(n) T.c and S.C
# def reverseWordsInString(s):
#     lst=s.split(' ')
#     # print(lst)
#     if len(lst)==1:
#         return lst[0]

#     i,j=0,len(lst)-1

#     while i<=j:
#         lst[i], lst[j]=lst[j], lst[i]
#         i+=1
#         j-=1

#     # print(lst)

#     return ' '.join(lst)

# def reverse(s,b,e):
#     while b<e:
#         s[b],s[e]=s[e],s[b]
#         b+=1
#         e-=1

#     # return s

# def reverseWordsInString(s):
#     s=list(s)
#     n=len(s)
#     b=0
#     for e in range(n):
#         if s[e]=='':
#             reverse(s,b,e-1)
#             b=e+1

#     reverse(s,b,e-1)
#     reverse(s,0,n-1)
#     return ''.join(s)

# s="welcome to"
# print(reverseWordsInString(s))

# Reverse words in a string


def reverse_word(s, start, end):
	while start < end:
		s[start], s[end] = s[end], s[start]
		start = start + 1
		end -= 1


s = "Welcome to dsa"


s = list(s)
start = 0
while True:
	
	try:
		end = s.index(' ', start)

		reverse_word(s, start, end - 1)

		start = end + 1

	except ValueError:

		reverse_word(s, start, len(s) - 1)
		break

s.reverse()

s = "".join(s)

print(s)

