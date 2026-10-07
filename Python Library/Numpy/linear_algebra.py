import numpy as np

A = np.array([[[1,2,3],
             [4,5,6],
             [7,8,9]]])
B = np.array([[[0,1,2],
             [3,4,5],
             [6,7,8]]])
#----------pairwise----------
# Addition of Matrix pairwise
print(A+B)

# Subtraction of Matrix
print(A-B)
# Multiplication of Matrix
print(A*B)

# transpose of Matrix
print(A.T)
print(B.T)

print(A.T*B)
print(A*B.T)