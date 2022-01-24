day=input("enter the day")
meal_time=input("enter the meal_time")
if day=="monday":
    if meal_time=="breakfast":
        print("poori subji")
    elif meal_time=="lunch":
        print("sambhar rice")
    else:
        print("chicken rice")
elif day=="tuesday":
    if meal_time=="breakfast":
        print("poha")
    elif meal_time=="lunch":
        print("rajma rice")
    else:
        print("roti")