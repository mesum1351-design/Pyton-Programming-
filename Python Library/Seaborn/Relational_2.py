import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
print(data.head())

sns.relplot(data = data, x = "total_bill", y = "tip", hue = "time", col = "smoker")
plt.show()

sns.relplot(data = data, x ="total_bill", y = "tip", hue = "size")
plt.show()

sns.relplot(data = data, x ="total_bill", y = "tip", size = "size", sizes=(100,300), hue ="size")
plt.show()

sns.relplot(data = data, x = "day", y = "total_bill")
plt.show()

sns.relplot(data = data, x = "day", y = "total_bill", kind = "line")
plt.show()

sns.relplot(data = data, x = "day", y = "total_bill", hue = "sex", kind = "line")
plt.show()

sns.relplot(data= data, x = "day", y = "total_bill", hue = "sex", kind ="line", col= "time")
plt.show()