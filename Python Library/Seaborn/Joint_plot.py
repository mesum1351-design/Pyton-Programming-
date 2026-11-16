import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

sns.jointplot(data = data, x = "total_bill", y = "tip")
plt.show()

sns.jointplot(data = data, x = "total_bill", y = "tip", hue = "sex")
plt.show()

sns.jointplot(data = data, x = "total_bill", y = "tip",hue = "sex",kind = "kde")
plt.show()

kind = ['scatter',"kde",'hist','hex','reg','resid']
for k in kind:
    sns.jointplot(data = data, x = "total_bill", y = "tip",kind = k)
    plt.show()