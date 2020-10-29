def check_speed(speed):
    point=speed-70
    points=point//5
    if(speed<70):
        print("ok")
    elif(speed>70) and (points<12):
            print("points:-",points)
    else:
        print("license suspended")
user_speed=int(input("enter speed"))
check_speed(user_speed)
