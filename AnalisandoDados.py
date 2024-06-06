import pandas as pd

atlcrime = pd.read_csv('atlcrime.csv')
print(atlcrime.head())
print(atlcrime['crime'].value_counts())
print(atlcrime.groupby(['crime'])['number'].agg(['mean', 'median']))
