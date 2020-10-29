def perfect(num):
    result=0
    for i in range (1,num):
        if(num%i==0):
            result=result+i
    if(result==num):
        print(num,"is perfect number")
    else:
        print(num,"is not perfect  number")
num=int(input("enter the number"))
perfect(num)
            