quantity=int(input("enter the quantity:"))
price=int(input("enter the price:"))
total_amount=quantity*price
if total_amount>1000:
   print("Total amount after getting 10% discount is:",total_amount-(total_amount/10))
elif total_amount<=1000:
    print(total_amount)
else:
    print("error")
