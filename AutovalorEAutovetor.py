import numpy as np

a = np.array([[6, -1], [2, 3]])
autovalores, autovetores = np.linalg.eig(a)
matriz_diagonal = np.diag((autovalores))
print('Autovalores')
print(autovalores)
print('\nAutovetores:')
print(autovetores)
print('\nMatriz diagonal:\n', matriz_diagonal)

primeiro_autovalor = autovalores[0]
autovetor_associado = autovetores[:, 0]
print('Primeiro autovalor: ', primeiro_autovalor)
print('Autovetor associado ao primeiro autovalor: ', autovetor_associado)
print(f"""Dividindo por {autovetor_associado[0]},
      {autovetor_associado/autovetor_associado[0]}""")
