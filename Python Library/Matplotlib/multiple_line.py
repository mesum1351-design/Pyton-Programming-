import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.arange(0,10,1)
y1 = x**2
y2 = x**3

plt.xlabel("x")
plt.ylabel("y")


plt.plot(x,y1, label="x")
plt.plot(x,y2, label="y")
plt.grid()
plt.legend()
plt.show()