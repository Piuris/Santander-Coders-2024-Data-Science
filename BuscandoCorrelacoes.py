import matplotlib.pyplot as plt
import seaborn as sns
iris = sns.load_dataset('iris')
# print(iris)
iris['species'].value_counts()
g = sns.pairplot(iris, hue='species')
g.map(sns.scatterplot)
plt.show()
