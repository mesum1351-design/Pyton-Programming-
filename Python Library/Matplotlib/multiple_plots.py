import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.subplot(2,1,1)
plt.plot(x,y,"o")
plt.grid(True)
plt.subplot(2,2,2)
plt.plot(x,y,"o")
plt.grid()
plt.show()