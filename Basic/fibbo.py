n=int(input("enter:" ))
f1=1
f2=1
s=0
while n-2>0:
    s=f1+f2
    f1=f2
    f2=s
    n-=1
print(s)
