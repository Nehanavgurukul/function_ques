def dictionary():
    d={}
    i=1
    while(i<=num):
        key=i
        value=i*i
        c={key:value}
        d.update(c)
        i=i+1
    print(d)
num=int(input("enter the number"))
dictionary()