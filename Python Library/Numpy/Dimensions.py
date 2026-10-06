# Dimensions
import numpy as np
#1D
a = np.array([1,2,3,4])
print(a.ndim)
#2D
b = np.array([[1,2,3,4],
              [5,6,7,8],
              ])
print(b.ndim)

c = np.array([[1,2,3,4],
              [5,6,7,8],
              [1,4,6,3]
              ])
print(c.ndim)

# Shape
print(a.shape) #(4,)
print(b.shape) #(2, 4)
print(c.shape) #(3, 4)
