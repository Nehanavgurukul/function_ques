def add_numbers_list(list1,list2):
   i=0
   c=[]
   sum=0
   while(i<len(list1)):
        j=i
        while(j<=i):
           sum = (list1 [i] + list2[j])
           c.append(sum)
           j=j+1
        i=i+1
   print(c)
l=[8,6,5,78]
k=[4,3,2,45]
add_numbers_list(l,k)