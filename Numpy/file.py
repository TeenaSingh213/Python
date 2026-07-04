x = open(r"C:\Users\teena\OneDrive\Documents\Sample.txt" , "r")
a = x.read(100)
print(a)
print(" ")

b = x.readlines()
print("This is the first line",'\t',b,'\n')
print("This is the second line",'\t',b,'\n')
print("This is the third line",'\t',b,'\n')