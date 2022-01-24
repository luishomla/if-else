quantity=int(input("enter the number"))
cost=quantity*100
if cost>100:
    dis=cost/10
    print(dis,"given discount")
else:
    print("not given discount")