import math
import numpy as np
import matplotlib.pyplot as plt

# print((6 - math.sqrt(3)) / 3)

def func(x):
    return x ** 3 - 6 * x ** 2 + 11 * x - 6

x1 = float("inf")
x2 = 0.0

for i in range(1000):
    x1 = x2
    x2 = x1 - (3 * x1 ** 2 - 12 * x1 + 11) / (6 * x1 - 12)
    x_diff = abs(x2 - x1)
    print(f"x_{i + 1} = {x2:.9f}, |x_{i + 1} - x_{i}| = {x_diff:.3e}")
    if x_diff < 1e-5:
        break

y = func(x2)
print(y)

x = np.linspace(x2 - 0.1, x2 + 0.1, 1000)
y = func(x)

plt.plot(x, y)
plt.grid()
plt.show()

