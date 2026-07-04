import numpy as np
a = np.linspace(0,5,10)[1:-1].round(2)
for i in a:
    print(i)
    
n = np.array([1,2,0,0,4,0])
for i in range(len(n)):
    if n[i] != 0:
        print(i)
    else:
        continue