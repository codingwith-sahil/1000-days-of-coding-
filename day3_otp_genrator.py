import random
otp=random.randint(1111,9999)
num=input("enter your phone number : ")
if len(num)!=10:
    print("please enter 10 digit phone number")
else:
    print("your otp is : ",otp)
