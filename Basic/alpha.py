n=int(input("enter:" ))
i=1

while i<n+1:
    j=1
    k=i
    while j<n+1:
        count=1
        if count<n+1:
            c=chr(ord('A')+k-1)
            print(c,end='')
            k+=1
            count+=1
        j+=1
    print()
    i+=1
print()
i=1
while i<n+1:
    j=1
    while j<n+1:
        c=chr(ord("A")+i-1)
        print(c,end='')
        j+=1
    print()
    i+=1
print()
i=1
while i<n+1:
    j=1
    k=i
    while j<=i:
        c=chr(ord("A")+i-1)
        print(c,end='')
        j+=1
    print()
    i+=1
print()
i=1
while i<n+1:
    j=1
    start_chr=chr(ord('A')+i-1)
    while j<=i:
            c=chr(ord(start_chr)+j-1)
            print(c,end='')
            j+=1
    print()
    i+=1
print()
i=1

# while i<n+1:
#     j=1
#     start_char=chr(ord('A')+i-j)
#     while j<n+1:
#             c=chr(ord(start_char)+j-1)
#             print(c,end='')
#             j+=1
#     print()
#     i+=1
print()
i=1
k=n
while i<=n:
    j=1
    
    
    
    while j<=i:
       
        
        c=chr(ord('A')+n-i +j-1)
        print(c,end='') 
       
       
        j+=1
        
    print()
    i+=1
print()
i=1
k=n
while i<=n:
    j=1
   
    while j<=n-i+1:
        print(k,end='')
        j+=1
        
    i+=1
    k-=1
    
    print()
        
        
