n=int(input("enter:" ))
# i=1
# while i<n+1:
#     j=1
#     while j<=i:
#         print(j,end=' ')
#         j+=1
#     i+=1
#     print()
# print( )
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print(" ")
