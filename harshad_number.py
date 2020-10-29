num=int(input("enter the number"))
c=num
sum=0
modulus=0
while(c!=0):
    modulus=c%10
    sum=sum+modulus
    c=c//10
if(num%sum==0):
    print("it is harshad number")
else:
    print("it is not harshad number")