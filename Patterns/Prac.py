n=int(input("enter:" ))
i=1
while i<n+1:
    j=1
    while j<=i:
        k=i
        while k>0:
            print(k,end='')
            k-=1
            j+=1
    print()
    i+=1