def check_numbers(num1,num2):
   i=0
   c=[]
   while(i<len(num1)):
        j=i
        while(j<=i):
            if(num1[i]%2==0 and num2[j]%2==0):
                print("dono even hai")
            else:
                print("dono even nahi")
            j=j+1
        i=i+1
    
x=[98,65,54,35,85]
y=[34,55,78,87,98]
check_numbers(x,y)