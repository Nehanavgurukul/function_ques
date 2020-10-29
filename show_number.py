def show_number(num):
    i=0
    while(i<=num):
        if(i%2==0):
            print(i,"even")
        else:
            print(i,"odd")
        i=i+1
num_1=int(input("enter the value"))
show_number(num_1)