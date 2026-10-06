import numpy as np
a = np.array([0,1,2,3,4,5])
b = np.array([0,1.0,2.4,3.8,4.6])
print (a)
print(a.dtype)
print(b.dtype)
#  type casting
b = np.array([0,1.0,2.4,3.8,4.6], dtype = int)
print(b)
print(a.shape)
print(b.shape)

