from turtledemo.chaos import plot

import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

sns.scatterplot(
    data=data,
    x="total_bill",
    y="tip",
    hue="sex",
)
print(data.head())
print (data.tail())

plt.show()