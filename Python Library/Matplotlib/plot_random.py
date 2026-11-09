import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = np.random.normal(0.5,0.1,(100))
x.sort()
y = x **2
print(x)
print(y)

plt.plot(x,y)
plt.show()

a = np.random.randint(1,10,10)
b= np.random.randint(1,10,10)
print (a)
print(b)
plt.plot(a,b)
plt.show()