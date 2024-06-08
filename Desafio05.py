'''Carregue o dataset 'titanic' da biblioteca seaborn e identifique alguma
correlação nos seus dados'''
import seaborn as sns
import matplotlib.pyplot as plt
titanic = sns.load_dataset('titanic')
select_columns = titanic[['age', 'alive']]
g = sns.PairGrid(select_columns, hue='alive')
g.map(sns.scatterplot)
g.add_legend()
plt.show()
