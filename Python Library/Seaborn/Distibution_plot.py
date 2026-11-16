import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

print(data.head())
print(data.tail())

sns.displot(data = data , x = "total_bill")
plt.show()

sns.displot(data = data , x = "total_bill", kind="kde")
plt.show()

sns.displot(data = data , x = "total_bill", hue = "sex")
plt.show()

sns.displot(data = data , x = "total_bill", col= "sex")
plt.show()

sns.displot(data=data, x = "total_bill", hue = "sex", col ="day")
plt.show()

sns.displot(data = data, x = "total_bill", hue = "sex", col = "day",kind = "kde", multiple = "stack")
plt.show()

sns.displot(data = data, x = "total_bill", y = "tip", hue = "sex", kind = "kde" )
plt.show()

sns.displot(data = data, x = 'total_bill', y = 'tip', hue = 'day', kind = 'kde', rug = True)
plt.show()

sns.displot(data = data, x = "total_bill", hue = "sex", kind = "ecdf")
plt.show()

sns.displot(data = data, x = "total_bill", hue = "sex", kind = "ecdf", col = "day")
plt.show()