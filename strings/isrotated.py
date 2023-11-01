def isRotated():
    s1, s2='ABCD','CDAB'
    if len(s1)!=len(s2):
        return False
    s3=""
    s3=s1+s1
    # return s3.find(s2)!=-1
    return s2 in s3
    
        



print(isRotated())