list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
new_list=[]

for i in (list1+list2):
    if( i in list1 and i  in list2):
        if(i not in new_list):
            new_list.append(i)
print(new_list)

