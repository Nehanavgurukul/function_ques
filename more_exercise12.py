words ="navgurukul is great "
i = 0
list=[]
a=" "
while i < len(words):
    if(words[i]==" "):
        list.append(a)
        a=" "
        i=i+1
    else:
        a=a+words[i]
        i=i+1
print (list)
        
    