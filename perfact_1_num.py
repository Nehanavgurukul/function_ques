def perfact(num):
    result=0
    index=1
    while(index<num):
        if(num%index==0):
            result=result+index
        index=index+1
    if(result== num):
        print("it is perfact",num)
    else:
        print("it is not perfact",num)
num=int(input("enter the any number"))
perfact(num)