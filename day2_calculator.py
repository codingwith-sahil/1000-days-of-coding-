num_1=int(input("enter the first number : "))
num_2=int(input("enter the second number of your choice :" ))
while True:
    print("enter 1 for addition")
    print("enter 2 for subtraction ")
    print("enter 3 for multiplication")
    print("enter 4 for divison ")
    print("enter 5 for exist")
    ch=int(input("enter your choice"))
    if ch==1:
        print("the additon of two numbers are ",num_1+num_2)
    elif ch==2:
        print("the subtraction of two numbers are",num_1-num_2)
    if ch==3:
        print("the mulitplication of two numbers are",num_1*num_2)
    elif ch==4:
        if num_2==0:
            print("you can't divide a number by zero")
        else:
            print("the divison of two numbers are",num_1/num_2)
    elif ch==5:
        break
    else:
        print("please enter the correct choice")
        
    
        
