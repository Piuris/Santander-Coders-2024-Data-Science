import numpy as np
lista = [1, 2, 3, 4, 5, 6]
array = np.array(lista)
print(type(lista))
print(type(array))
arr_zeros = np.zeros(10)
print(arr_zeros)
print(array[0])
array[0] = 9
print(array)

# Matrizes
matriz_zeros = np.zeros((5, 3))
print(matriz_zeros)

# Notas de alunos
lista_de_notas = [9.8, 5.6, 7.8, 9.1, 6.5]
notas = np.array(lista_de_notas)
print('Maximo', notas.max())
print('Minimo', notas.min())
print('Desvio padrao', notas.std())
print('Posicao menor', notas.argmin())
