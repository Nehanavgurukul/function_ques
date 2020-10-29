user_password=input("enter the nay password")
if((len(user_password)>=6 )and (len(user_password)<=16) and ("$" in user_password)and ("A"  in user_password )):
     print("strong password")
else:
    print("weak password")