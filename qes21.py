cp=float(input("enter the cost price of the product"))
sp=float(input("enter the selling price of the product"))
if(sp>cp):
    amount=sp-cp
    print("profit amount")
elif(cp<sp):
    amount=cp-sp
    print("loss amount")
else:
    print("no less no profit")
