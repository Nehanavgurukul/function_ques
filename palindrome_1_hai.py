def palindrome(num):
    list1=[]

    index=len(num)-1
    while(index>=0):
        list1.append(num[index])
        index=index-1
    if(list1==num):
        print("it is palindrome")
    else:
        print("it is not palindrome")
num=[3,5,7,9,7,5,3]
palindrome(num)
