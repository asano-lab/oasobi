import numpy as np

G = np.matrix([
    [1, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 1]
], dtype="u1")

print(G)
print(G.dtype)
print(G.shape)

k = G.shape[0]

A = np.matrix(np.identity(k))
for i in range(k):
    col_i = np.array(G)[:,i]
    if col_i[i] == 1:
        A_i = np.identity(k)
        A_i[:,i] = col_i
        A = A_i * A % 2
        G = A_i * G % 2

print(G)
