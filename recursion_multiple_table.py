def multi (n,i):
    print(n*i)
    i=i+1
    if(i<=10):
        multi(n,i)
multi(12,1)