'''Encontre uma base de dados e explore ela validando hipóteses.'''
import pandas as pd

atlcrime = pd.read_csv('atlcrime.csv')
print(atlcrime.head())
print(atlcrime['crime'].value_counts())
crime_counts = atlcrime.groupby(['date'])['crime'].size().reset_index(
    name='count_crimes')
print(crime_counts)
npu = atlcrime.groupby(['npu'])['crime'].size().reset_index(
    name='Neighborhood Planning Unit')
print(npu)
