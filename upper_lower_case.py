def upper_lower(str):
    upper=0
    lower=0
    for i in str:
        if i.isupper():
            upper=upper+1
        elif i.islower():
            lower=lower+1
        else:
            pass
    print("original string ",str)
    print("upper case charactor",upper)
    print("lower case charactor",lower)
upper_lower("Neha Yadav Ji")