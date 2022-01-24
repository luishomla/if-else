# Q1.Write a program to checkif a year is leap year or not


year=int(input("enter the year"))
if year%4==0 and year%400==0:
    print("is leap year",year)
elif year%4!=0:
    print("not leap year")
else:
    if year%100==0:
        print("century leap year")
        if year%400!=0:
            print("not leap year")