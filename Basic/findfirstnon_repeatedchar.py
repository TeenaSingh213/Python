m=input("Enter a string:")
for i in m:
    if m.count(i)==1:
        print("the first non-repeated characater is:",i)
        break
else:
    print("There is no non-repeated character in the string.")