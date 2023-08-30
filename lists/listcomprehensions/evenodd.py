def getEvenOddLst(lst:list):
    even=[i for i in lst if i%2==0]
    odd=[i for i in lst if i%2!=0]

    return even,odd


if __name__=='__main__':
    lst=[1,3,5,7,2,9,4,6,12,33,45,17]
    even,odd = getEvenOddLst(lst)

    print(even, odd)
