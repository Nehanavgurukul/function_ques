def outter_fun(a,b):
    def inside_fun():
        a+b
    inside_fun()
    return ((a+b)+5)
a=outter_fun(11,9)
print(a)


  