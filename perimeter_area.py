
def perimeter_area(a,b):
    area=a*b
    c =area
    perimeter=2*(area)
    p=perimeter
    return (c,p)
length=int(input("enter the lenth "))
wide=int(input(" enter the wide "))
print(perimeter_area(length,wide))