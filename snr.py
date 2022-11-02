import numpy as np
import matplotlib.pyplot as plt

BIT_LEN = 16
MAX_BIT = (1 << BIT_LEN) - 1

MAX_GOSA = 1 / MAX_BIT / 2

x = np.logspace(1, np.log10(MAX_BIT), 1000)
# print(x)

# print(x.astype("u8"))
y = x / MAX_GOSA
# print(y)
y = 20 * np.log10(y)

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111)

ax.set_xscale("log")
# ax.set_yscale("log")

ax.plot(x, y)
plt.show()
