import pandas as pd

# Cria um dicionario com autores, preços e títulos
aut = ['Rick Riordan', 'J. R. R. Tolkien', 'Rick Riordan', 'Machado de Assis']
tit = ['O ladrão de Raios', 'A sociedade do Anel', 'Mar de Monstros',
       'Memórias Postumas de Brás Cubas']
precos = [41.2, 35.7, 39.5, 40.5]
dictionary = {'Autores': aut, 'Títulos': tit, 'Preços': precos}

# DataFrame
df = pd.DataFrame(dictionary)
print(df)
print('-' * 30)
print(df['Autores'])
print('-' * 30)
print(df['Autores'][1])
print('-' * 30)
print(df['Preços'].mean())
mask = df['Autores'] == 'Rick Riordan'
print(df[mask])
nova_linha = pd.DataFrame({'Autores': ['Rick Riordan'],
                           'Títulos': ['A maldiça do Titã'],
                           'Preços': [40.20]})
df = pd.concat([df, nova_linha], ignore_index=True)
print(df)
mascara_correcao = df['Títulos'] == 'A maldiça do Titã'
df.loc[mascara_correcao, 'Títulos'] = 'A Maldição do Titã'
print(df)
