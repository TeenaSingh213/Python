#square the items of a list
print(list(map(lambda x:x**2,[1,2,4,3,5])))

print(list(map(lambda x:'even' if x%2 == 0  else 'odd',[1,3,6,4,7])))
l=[3,5,32,5,23,4]
print(list(filter(lambda x:x>5,l))) 
import functools
print(functools.reduce(lambda x,y: x if x<y else y,[12,43,56,3256,677,34]))
