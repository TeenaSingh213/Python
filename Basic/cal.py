a=int(input("enter the first no:" ))
b=int(input("enter the second no:" ))


c=input("enter the operator:" )
if(c=="1"):
    print(a+b)
elif(c=="2"):
    print(a-b)
elif(c=="3"):
    print(a*b)
elif(c=="4"):
    if(b>0):
        print(a/b)
    else:
        print("Invalid no")
else:
    print("Invalid no. is printed")


