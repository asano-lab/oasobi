import numpy as np

G = np.matrix([
    [1, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 1]
], dtype="u1")

print(G)
print(G.dtype)
print(G.shape)

A = np.matrix([
    [1, 0, 0],
    [1, 1, 0],
    [0, 0, 1]
])

print(A * G % 2)
