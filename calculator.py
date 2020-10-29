def calculator(number_x,number_y,operation):
    if(operation=="add"):
       number_1=number_x+number_y
       add_result=number_1
      #  print(add_result)
       return add_result
    elif(operation=="subtract"):
       number_2=number_x-number_y
       subtract_result=number_2
      #  print(subtract_result)
       return subtract_result
    elif(operation=="maltiple"):
       number_3=number_x*number_y
       malptiple_result=number_3
      #  print(maltiple_result)
       return malptiple_result
    elif(operation=="divide"):  
       number_4=number_x/number_y
       divide_result=number_4
      #  print(divide_result)
       return divide_result

user_1=int(input("number dalo"))
user_2=int(input("number dalo"))
user_3=input("enter the operation")
print(calculator(user_1,user_2,user_3))

