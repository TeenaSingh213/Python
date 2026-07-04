n=int(input("Enter a no"))
for i in range(1, 11):
    if i == 5:
        continue
    print(n, "x", i, "=", n*i)