x=int(input("enter 1st side:"))
y=int(input("enter 2nd side:"))
z=int(input("enter 3rd side:"))
if x==y==z:
    print("equilateral")
elif x==y or y==z:
    print("isosceles")
else:
    print("scalence")
