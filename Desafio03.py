'''Monte uma tabela contendo alguns livros, alguns autores e os preços dos
livros e adicione um novo livro na tabela.'''
import pandas as pd

dict = {'Autores': ['Daniel Keyes', 'Sadi Pierozan', 'Nicolau Maquíavel'],
        'Títulos': ['Flores para Algernon', 'A Lei do Tempo', 'O Príncipe'],
        'Preços': [52.90, 45.73, 19.82]}
df = pd.DataFrame(dict)
print(df)
nova_linha = pd.DataFrame({'Autores': ['Stephen King'],
                          'Títulos': ['It A Cois'], 'Preços': [84.58]})
df = pd.concat([df, nova_linha], ignore_index=True)
print(df)
mascara_correcao = df['Títulos'] == 'It A Cois'
df.loc[mascara_correcao, 'Títulos'] = 'It A Coisa'
print(df)
