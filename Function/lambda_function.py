a=lambda x:x**2
print(a(4))
b=lambda a,b:a+b
print(b(3,5))
x=lambda s:'a' in s
print(x("Helloa"))
c=lambda m:'even' if m%2 == 0 else 'odd'
print(c(7))
# lambda function is used in higher order function 
def square(x):
    return x**2
def transform(f,L):
    output=[]
    for i in L:
        output.append(f(i))
    print(output)
L=[1,2,3,4,5]
transform(lambda x: x**2 , L)