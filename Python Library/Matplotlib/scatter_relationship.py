import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


hours = [1,2,3,4,5]
marks = [40,50,60,70,80]
size = [100,200,300,200,100]
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.title("SCATTER PLOT")
plt.plot(hours,marks,"o")
plt.show()
plt.pie(marks, labels = marks, autopct = '%1.1f%%', explode=(0.0,0.1,0.0,0.0,0.0))
plt.show()
plt.show()
plt.scatter(hours,marks,color="red", s=size, marker="o",)
plt.show()

x = np.array([1,2,3,4,5,6,7,8])
y = np.array([2,4,3,7,10,12,13,12])
plt.scatter(x,y)
plt.show()