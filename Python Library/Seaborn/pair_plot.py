import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

sns.pairplot(data= data)
plt.show()

sns.pairplot(data= data, hue= "day")
plt.show()


