letter=input("Enter a letter:" )
vowel=['a','e','i','o','u']
t = 0
for i in vowel:
    if(i==letter):
        print("Letter is vowel")
        t=1
if t == 0:
    print("consonent")