expected_date =int(input("enter the expected date="))
return_date=int(input("enter the return date"))
if return_date>expected_date:
    a=return_date-expected_date
    b=a*15
    print("fine is rs=",b)
return_month=int(input("enter the return month="))
expected_month=int(input("enter the return month="))
if return_month>expected_month:
    c=return_month-expected_month
    d=c*500+b
    print("monthly days fine is",d)


