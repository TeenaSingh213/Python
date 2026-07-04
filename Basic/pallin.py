n=int(input("ENTER:" ))
m=0
dup=n
while n>0:
    a=n%10
    m=(m*10)+a
    n=n//10
print(m)

print(m==dup)




