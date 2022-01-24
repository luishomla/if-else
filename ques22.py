physic=int(input("phy.marks:-"))
chemistry=int(input("che.marks:-"))
biology=int(input("bio.marks:-"))
maths=int(input("maths marks:-"))
computer=int(input("com.marks:-"))
total=physic+chemistry+biology+maths+computer
per=total/5
print(per)
if per>=90:
    print("grade A")
elif per>=80:
    print("grade B")
elif per>=70:
    print("grade C")
elif per>=60:
    print("grade D")
elif per>=40:
    print("grade E")
else:
    print("grade F")
    