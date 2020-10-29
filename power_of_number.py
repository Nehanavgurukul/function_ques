def power_of_number(num1,num2):
    if(num2>0 and  num1>0):
        power_of_number=num1**num2
        a=power_of_number
        return a
    else:
        return 0
n1=int(input("enter the number"))
n2=int(input("enter the number"))
print(power_of_number(n1,n2))
        
    