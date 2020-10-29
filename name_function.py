def function_name(name1,name2):
    if(len(name1)==len(name2)):
        print(name1)
        print(name2)
    elif(len(name1)>len(name2)):
        print(name1)
    elif(len(name1)<len(name2)):
        print(name2)
    
user1_string=input("enter the string")
user2_string=input("enter the string")
function_name(user1_string,user2_string)
