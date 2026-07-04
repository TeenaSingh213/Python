s=int(input("Start Fahrenheit value:" ))
e=int(input("End Fahrenheit value:" ))
w=int(input("Step Size :" ))
while s<e+1:

    cel=int((s-32)*5/9)
    print(f"{s} \t {cel}")
    s=w+s