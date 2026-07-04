n=int(input("enter:" ))
even=0
odd=0
while n>0:
    a=n%10
    if a%2==0:
        even+=a
    else:
        odd+=a
    n=n//10
print(f"{even}\t{odd}")
