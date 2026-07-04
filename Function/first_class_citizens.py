def square(num):
    return num**2
print(type(square))
print(id(square))
x=square
print(id(x))
print(x(4))
#WE can also delete a function using del(function_name)
#Recalling a function
def f():
    def x(a,b):
        return a+b
    return x
val= f()(3,4)
print(val)
#Function Argument
def func_a():
    print('inside func_a')

def func_b(z):
    print('inside func_c')
    return z()

print(func_b(func_a))
