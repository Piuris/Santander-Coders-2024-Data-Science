import numpy as np

is_covid_positive = np.array(['Yes', 'No', 'No', 'Yes', 'Yes', 'No'])
mask = is_covid_positive == 'Yes'
is_covid_positive[mask] = 'C19'
print(is_covid_positive)
notas = np.array([4.9, 6.5, 3.2, 6.7])
for i in range(0, len(notas)):
    if notas[i] >= 5 and notas[i] <= 6.5:
        print(notas[i])
