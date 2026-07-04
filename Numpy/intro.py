import numpy as np
a = np.arange(12).reshape(3,4)

b = np.arange(12,24).reshape(3,4)

c=np.arange(27).reshape((3,3,3))

print(c)
# print(c[::2,::3])
# print(c[::2,1::2])
# print(c[1,::3])


# print(c[::2,0,::2])
for i in np.nditer(c):
    print(i)