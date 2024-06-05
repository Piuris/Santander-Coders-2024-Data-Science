'''Crie um programa que peça pro usuario digitar 10 notas de alunos e
transforme eles num array do numpy e calcule a media, desvio padrão, maior
nota, menor nota, posições, etc.'''
import numpy as np

lista_notas = list()
for i in range(0, 10):
    lista_notas.append(float(input(f'Digite a {i + 1}ª nota: ')))

notas = np.array(lista_notas)
print(f'{'Impressão das notas'}')
print('-' * 40)
for i in range(0, len(notas)):
    texto = f'{i + 1}ª nota:'
    print(f'{texto:<10}{notas[i]:>30}')
print('-' * 40)
print(f'A maior nota é: {notas.max()} na {notas.argmax()+1}ª posição')
print(f'A menor nota é: {notas.min()} na {notas.argmin()+1}ª posição')
print(f'O desvio padrão das notas é: {notas.std():.2f}')
