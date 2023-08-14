def counter():
    # string method
    # x = int(input("enter number: "))
    # x = len(str(x))

    # print(x)

    # normal mtd
    nos = int(input("enter number "))
    count = 0

    while(nos > 0):
        nos//=10
        print(nos)
        count+=1

    print("total digits are : ", count)

counter()