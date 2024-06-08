import pandas as pd


def limpa_preco(linha):
    linha['price'] = linha['price'].replace('R$ ', '')
    linha['price'] = linha['price'].replace('\n', '')
    linha['price'] = linha['price'].replace('/Mês', '')
    linha['price'] = linha['price'].replace('                   ', '')
    linha['price'] = linha['price'].replace('/Mês', '')
    return linha


def ajusta_alugueis(linha):
    linha['price'] = linha['price'].replace('.', '')
    preco = int(linha['price'])
    if preco > 10000:
        preco = preco * 200
    linha['price'] = preco
    return linha


df = pd.read_excel('Sao_paulo.xlsx')
print(df)
auxiliar = df.loc[10031]
limpa_preco(auxiliar)
df.apply(lambda x: limpa_preco(x), axis=1)
auxiliar = df.loc[10031]
ajusta_alugueis(auxiliar)
