n=int(input("Enter a number: "))
sum=0
for i in range(n+1):
    if i%2==0:
        sum+=i
    else:
        continue
print("Sum of even numbers is:", sum)