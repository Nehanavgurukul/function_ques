def factorial(num):
    fac=1
    while(0<num):
        fac=fac*num
        num=num-1
    return fac
n=int(input("enter the num"))
print(factorial(n))