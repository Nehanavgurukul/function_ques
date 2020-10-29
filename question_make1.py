def iligible_for_vote():
    if(user_age<18):
        print("not iligible")
    elif(user_age>=18):
        print("you are iligible")
user_age=int(input("enter the age"))
iligible_for_vote()