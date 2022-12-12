import math

# print((6 - math.sqrt(3)) / 3)

x1 = float("inf")
x2 = 0.0

for i in range(1000):
    x1 = x2
    x2 = x1 - (3 * x1 ** 2 - 12 * x1 + 11) / (6 * x1 - 12)
    x_diff = abs(x2 - x1)
    print(f"x_{i + 1} = {x2:.9f}, |x_{i + 1} - x_{i}| = {x_diff:.3e}")
    if x_diff < 1e-5:
        break

y = x2 ** 3 - 6 * x2 ** 2 + 11 * x2 - 6
print(y)
