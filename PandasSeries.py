import pandas as pd

lista = [12, 23, 34, 45, 56, 67]

serie_pandas = pd.Series(lista)
print(serie_pandas)
print(serie_pandas[0])
notas = {'Tiago': 8, 'Guilherme': 9.5, 'Juca': 6.2}
serie_notas = pd.Series(notas)
print(serie_notas)
print(serie_notas['Tiago'])
print(serie_notas.mean())
print(serie_notas.median())
print('-' * 30)
print(serie_notas.describe())
print(serie_notas.sum())
