def getsmaller(lst, x):
    return [i for i in lst if i<x]

if __name__=='__main__':
    lst=[10,20,3,4,88,97,63,21,29,33,1002]
    x=33
    print(getsmaller(lst, x))
