import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

sns.catplot(data = data, x = "day", y = "total_bill")
plt.show()

sns.catplot(data = data, x = "day", y = "total_bill", hue = "sex")
plt.show()

sns.catplot(data = data, x = "day", y = "total_bill", kind = "box")
plt.show()

sns.catplot(data = data, x = "day", y = "total_bill", kind = "box", hue = "sex")
plt.show()

sns.catplot(data = data, x = "day", y = "total_bill", kind = "violin")
plt.show()

sns.catplot(data = data, x = "day", y = "total_bill", kind = "violin", hue = "sex", split = True)
plt.show()

sns.catplot(data = data, x = "day", y = "total_bill", kind = "bar")
plt.show()

sns.catplot(data = data, x = "day", y = "total_bill", kind = "bar", hue = "sex")
plt.show()