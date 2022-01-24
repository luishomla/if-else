liter=int(input("enter the water liter"))
if liter<=1:
    print("more water needs to be filled")
elif liter>1 and liter<10:
    print("no need to fill")
else:
    print("water will overflow")