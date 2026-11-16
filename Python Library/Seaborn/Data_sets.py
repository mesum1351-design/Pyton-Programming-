import seaborn as sns
import matplotlib.pyplot as plt

dataset1 = sns.load_dataset("tips")
dataset1.info()

dataset2 = sns.load_dataset("iris")
dataset2.info()
