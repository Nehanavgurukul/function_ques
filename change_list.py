def change_list(list_1,list_2):
    i=0
    list=[]
    d=0
    while(i<len(list_1)):
        j=i
        while(j<=i):
            d=(list_1[i]*list_2[j])
            list.append(d)
            j=j+1
        i=i+1
    print(list)
list_x=[5,10,50,20]
list_y=[2,20,3,5]
(change_list(list_x,list_y))