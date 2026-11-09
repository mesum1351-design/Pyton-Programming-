import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.arange(5)
y = x**2
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y,"o")
plt.grid()

plt.show()