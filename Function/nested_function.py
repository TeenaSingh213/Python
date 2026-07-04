def g(x):
    def h():
        x='abc'
    x  = x+1
    print('in g(x): x = ', x)
    h()
    return x
x=3
z=g(x)
def g(y):
    def i(y):
        y=y+1
        print('in i(y): y= ' , y)
    y = y + 1
    print('in g(y): y = ', y)
    i(y)
    return y
y=3
p=g(y)
print('in main program scope y = ', y)
print('in main program scope: p = ', p )