def prime (num):
    if(num==1):
        return False
    elif(num==2):
        return True
    else:
        for index in range(2,num):
            if(num% index==0):
                return False
        return True
num=int(input("enter the number"))
print(prime(num))
            
            