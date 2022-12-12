import math

print((6 - math.sqrt(3)) / 3)

x1 = float("inf")
x2 = 0.0

while abs(x2 - x1) >= 1e-5:
    print(x1, x2)
    x1 = x2
    x2 = x1 - (3 * x1 ** 2 - 12 * x1 + 11) / (6 * x1 - 12)
