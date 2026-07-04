import numpy as np
arr = np.array([12,4,2,12])
print(arr)
print("The dimension of arr is", arr.ndim)

arr2 = np.array([[1,2,3],[32,54,7]])
print(arr2)
print("The dimension of arr2 is", arr2.ndim)

z = np.zeros((3,4))
print(z)

print(np.eye(3))

a = np.arange(1,7).reshape(2,3)
print(a)
b = np.arange(6,12).reshape(3,2)
print(b)
print("Matrix multiplication of a and b is: ", a @ b)

e = np.array([0,1,2,3])
print(e.shape)