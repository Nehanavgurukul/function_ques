def max (x,y,z):
    if (x>=y and x>=z):
        print("it is max",x)
    elif(y>=x  and y>=z):
        print("it is max ",y)
    else:
        print("it is max",z)
max(5,9,7)