# marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
# index1=0
# while(index1<len(marks)):
#     index2=0
#     while(index2<len(marks[index1][index2])):
#         max.marks[index1][index2]
#         print(max.marks)
#         index2=index2+1
#     index1=index1+1

marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
index1=0
while(index1<len(marks)):
    index2=0
    max_marks=0
    while(index2<len(marks[index1])):
        if(max_marks<marks[index1][index2]):
            max_marks=marks[index1][index2]
        index2=index2+1
    print(max_marks)
    index1=index1+1