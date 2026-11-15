import seaborn as sns
import matplotlib.pyplot as plt
from seaborn import lineplot

data = {
    "hours": [1,2,3,4,5],
    "marks": [70,75,70,85,90]
}
sns.load_dataset("iris")
plt.title("Scatter Plot")
plt.show()
