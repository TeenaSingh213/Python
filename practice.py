# num=46
# sum=0
# x=num
# fin=0
# while x>0:
#     sum=sum+ x%10
#     x=x//10
# while sum>0:
#     fin=fin + sum%10
#     sum=sum//10
# print(fin)
s = input("Enter a word: ")
l=list(s)
print(l)
while "*" in l:
    l.remove("*")
print(l)
a= "".join(l)
print(a)
print(type(a))