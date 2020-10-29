def unique(list1):
    list=[]
    index=0
    while(index<len(list1)):
        if(list1[index] not in list):
            list.append(list1[index])
        index=index+1
    return list
print(unique([1,2,3,3,3,4,5]))