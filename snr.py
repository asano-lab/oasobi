import numpy as np
import matplotlib.pyplot as plt

BIT_LEN = 32
MAX_BIT = (1 << BIT_LEN) - 1

MAX_GOSA = 1 / MAX_BIT / 2

x = np.logspace(1, np.log10(MAX_BIT), 1000) / MAX_BIT
# print(x)

# print(x.astype("u8"))
y = x / (MAX_GOSA + x * 1e-5)
# print(y)
y = 20 * np.log10(y)

x = 20 * np.log10(x)

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111)

# ax.set_xscale("log")
# ax.set_yscale("log")

ax.plot(x, y)
ax.grid()
plt.show()
