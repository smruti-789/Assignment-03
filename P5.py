age1=int(input("Enter age1:"))
age2=int(input("Enter age2:"))
age3=int(input("Enter age3:"))
if (age1<age2) and (age1<age3):
    print(age1,"is younger")
    if (age2<age3):
        print(age3,"is oldest")
    else:
        print(age2,"is oldest")
elif (age2<age1) and (age2<age3):
    print(age2,"is younger")
    if (age1<age3):
        print(age3,"is oldest")
    else: 
        print(age2,"is oldest")
elif (age3<age1) and (age3<age2):
    print(age3,"is younger")
    if (age1<age2):
        print(age2,"is oldest")
    else:
        print(age1,"is oldest")