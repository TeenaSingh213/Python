def is_even(num):
    """This function returns if the given function is odd or even
    input-any valid int
    output-odd/even
    """
    if type(num)==int:
        if num%2==0:
            return 'even'
        else:
            return 'odd'
    else:
        return "Please enter an integer value"
print(is_even(4))
for i in range(1,11):
    x=is_even(i)
    print(i,x)
#Defaul Argument
def add(a=1,b=0):
    return a+b
#Positional Argument
print(add(1,3))
#Keyword Argument
print(add(b=4,a=0))
# *args
def mul(*args):
    product=1
    for i in args:
        product = product*i
        
    return product
# **kwargs
def display(**kwargs):
    for(key,value) in kwargs.items():
        print(key,"->",value)
    return 0
print(display(India="Delhi",SriLanka="Colombo")) 