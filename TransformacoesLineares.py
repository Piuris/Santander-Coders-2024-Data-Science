import matplotlib.pyplot as plt

vetor = [2, 2]
origens = [(0, -1), (0, 1), (0, 0), (0, 2)]
origens_x = [origem[0] for origem in origens]
origens_y = [origem[1] for origem in origens]

plt.figure()
plt.quiver(origens_x, origens_y, [vetor[0]] * len(origens_x), [vetor[1]] *
           len(origens_y), angles='xy', scale_units='xy', scale=1, color='g')


plt.xlim(-1, 5)
plt.ylim(-2, 5)
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Um vetor com diferentes pontos de origem")
plt.show()
