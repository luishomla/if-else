user1=int(input("enter the item quantity:"))
user2=int(input("enter the total amount:"))
total=user1*user2
if total>1000:
    discount=total-total*10//100
    print("it is above 1000 there will be 10 percent discount:",discount)
else:
    print(total)
