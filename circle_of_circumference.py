def circle_of_circumference(redius):

    area_of_circle=180*redius**2
    circumference_of_circle=2*180*redius
    return area_of_circle,circumference_of_circle
redius=int(input("enter the lenth "))
print(circle_of_circumference(redius))