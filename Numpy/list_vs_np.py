l1=[i for i in range(100)]
l2=[i for i in range(100,200)]
c=[]
import time
start=time.time()
for i in range(len(l1)):
    c.append(l1[i] + l2[i])
print(time.time()-start)
    
import numpy as np
a=np.arange(100)
b=np.arange(100,200)
s=time.time()
c = a+b
print(time.time()-s)