list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
new_list=[]
for i in (list1+list2):
    if(i not in new_list):
        new_list.append(i)
print(new_list)
