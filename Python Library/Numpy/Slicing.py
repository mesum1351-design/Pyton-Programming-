import numpy as np
arr = np.array([0,1,2,3,4,5])

print(arr)
print (arr[0:])  # first index element to till end
print(arr[2:4])
print(arr[:4])
print(arr[:-3])  # neg(-) sign indicate from right or end
print(arr[-3:])

print(arr[1::3])  # only print index values

A = np.array([[0,1,2,3],
              [4,5,6,7]])
print(A)
print(A.shape)
print(A[0])
print(A[1])