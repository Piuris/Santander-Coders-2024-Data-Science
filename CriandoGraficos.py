import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('netflix_data.csv')
df = df.drop(df.columns[0], axis=1)
'''eixo_x = df['genre'].value_counts().keys()
eixo_y = df['genre'].value_counts().values
plt.bar(eixo_x, eixo_y, width=0.5)
plt.title('Filmes e Séries por gênero')
plt.xlabel('Gêneros')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
print(plt.show())'''
eixo_x = df['release_year'].value_counts().sort_index().keys()
eixo_y = df['release_year'].value_counts().sort_index().values
plt.plot(eixo_x, eixo_y)
plt.title('Filmes e séries por ano lançamento')
plt.xlabel('Ano de lançamento')
plt.ylabel('Quantidade')
print(plt.show())
