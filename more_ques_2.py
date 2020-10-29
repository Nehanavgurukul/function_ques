num_of_students=int(input("enter the student"))
kharcha_of_student=int(input("enter the kharcha"))
i=1
kharcha_of_oneday = num_of_students*kharcha_of_student
monthly_kharcha=0
while(i<=30):
    # kharcha_of_students=int(input("enter the kharcha"))

    monthly_kharcha=monthly_kharcha+kharcha_of_oneday
    i=i+1
if(monthly_kharcha<=5000):
    print("hum budget ke undar hai")
else:
    print("hum budget ke bahar hai")

