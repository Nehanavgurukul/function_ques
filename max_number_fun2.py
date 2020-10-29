def max_num():
    index=0
    max_n=0
    while(index<len(list)):
        if(max_n<list[index]):
            max_n=list[index]
        index=index+1
    print(max_n)
list=[3, 5, 7, 34, 2, 89, 2, 5]
max_num()