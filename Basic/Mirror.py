n=int(input("enter: "))
i=1
while i<=n:
    spaces=1
    while spaces<=n-i:
        print(" ",end="")
        spaces+=1
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    print()
    i+=1