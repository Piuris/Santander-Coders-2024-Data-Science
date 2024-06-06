'''Crie uma lista com notas de alunos e faça uma máscara booleana que filtre
as pessoas que ficaram de recuperação.'''
import numpy as np
lista = list()
while True:
    lista.append(float(input('Digite uma nota: ')))
    escolha = str(input('Deseja adicionar mais notas? [S/N] ')).upper()
    if escolha in 'SN':
        if escolha == 'N':
            break
    else:
        while escolha not in 'SN':
            escolha = str(input('Digite apenas S ou N: ')).upper()
notas = np.array(lista)
mask = notas < 5
for i in range(0, len(mask)):
    if mask[i]:
        print(f'O aluno {i + 1} está de recuperação')
