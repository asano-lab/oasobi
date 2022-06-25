import numpy as np

G = np.matrix([
    [1, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 1]
], dtype="u1")

print(G)
# print(G.dtype)
# print(G.shape)

k = G.shape[0]

A = np.matrix(np.identity(k), dtype="u1")
G_copy = G.copy()
for i in range(k):
    col_i = np.array(G_copy)[:,i]
    if col_i[i] == 1:
        A_i = np.identity(k)
        A_i[:,i] = col_i
        A_i = np.matrix(A_i, dtype="u1")
        A = A_i * A % 2
        # print(f"A_i=\n{A_i}")
        # print(f"A=\n{A}")
        G_copy = A_i * G_copy % 2
        print(f"掃き出し{i + 1}回目")
        print(G_copy)

print(A)
print(A * G % 2)
