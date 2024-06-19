import numpy as np
import matplotlib.pyplot as plt
from matplotlib.transforms import Affine2D

square = np.array([[0, 1, 1, 0, 0], [0, 0, 1, 1, 0]])


def plot_square(ax, square, color, label):
    ax.plot(square[0], square[1], color=color, label=label)


fig, axs = plt.subplots(2, 2, figsize=(10, 10))
plt.subplots_adjust(hspace=0.5)
transformations = [
    ("Rotação", Affine2D().rotate_deg(45)),
    ("Escalonamento", Affine2D().scale(2, 0.5)),
    ("Reflexão", Affine2D().scale(1, -1)),
    ("Cisalhamento", Affine2D().skew_deg(45, 0))
]

for i, (name, transformation) in enumerate(transformations, start=1):
    ax = axs.flatten()[i-1]
    transformed_square = transformation.transform(square.T).T
    plot_square(ax, transformed_square, color='blue', label='Transformado')
    plot_square(ax, square, color='red', label='Original')
    ax.set_title(name)
    ax.set_xlim(-2, 3)
    ax.set_ylim(-2, 3)
    ax.set_aspect('equal')
    ax.grid(True)
    ax.legend()
plt.show()

'''v = np.array([[1], [1]])
theta = np.pi / 4
r = np.array([[np.cos(theta), -np.sin(theta)],
             [np.sin(theta), np.cos(theta)]])
rotated_v = np.dot(r, v)

s = np.array([[2, 0], [0, 0.5]])
scaled_v = np.dot(s, v)

f = np.array([[1, 0], [0, -1]])
reflected_v = np.dot(f, v)

h = np.array([[1, 0.5], [0, 1]])
sheared_v = np.dot(h, v)

print('Rotação:')
print(rotated_v)
print('Escalonamento:')
print(scaled_v)
print('Reflexão:')
print(reflected_v)
print('Cisalhamento:')
print(sheared_v)
'''
