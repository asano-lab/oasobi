import numpy as np
import matplotlib.pyplot as plt

BIT_LEN = 16
MAX_BIT = (1 << BIT_LEN) - 1

x = np.logspace(1, np.log10(MAX_BIT), 1000)
# print(x)

# print(x.astype("u8"))
y = abs(x - (x + 0.5).astype("u8"))
print(y)

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111)

ax.set_xscale("log")
ax.plot(x, y)
plt.show()
