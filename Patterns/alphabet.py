n=int(input("enter:" ))
i=1
while i<n+1:
    j=1
    while j<=i:
        k=i
        a=chr(ord('A')+n)
        print(a)
        while k>0:
            c=chr(+k-1)
            print(c,end='')
            k-=1
            j+=1
    print()
    i+=1