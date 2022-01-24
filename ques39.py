language=input("choose language:")
if language=="english":
     print ("Welcome to Punjab National Bank:")
     secrect_pin=input("enter the digit pin")
     if secrect_pin=="1234":
         select=input("withdrawal or balance enquiry or deposit")
         balance="50000"
         if select=="withdraw":
             amount=int(input("enter the amount:"))
             if amount<=20000:
                 print("processing")
                 print("transfer complete")
                 print(50000-amount,"is your remaining balance")
             else:
                 print("sorry 20000 above cannot be withdraw")
         if select=="balance enquiry":
              print("your current balance is:",balance)
         if select=="deposit":
              deposit=int(input("enter deposit amount:"))
              print(deposit+50000,"is your current balance")
              print("thank you visit again")
         if select=="exit":
              print("thank you visit again")
else:
    print("wrong pin") 



        


    
    

