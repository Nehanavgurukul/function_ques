def even_list(list):
    list1=[]
    index=0
    while(index<len(list)):
        if(list[index]%2==0):
            list1.append(list[index])
        index=index+1
    return list1
print(even_list([1,2,3,4,5,6,7,8,9]))