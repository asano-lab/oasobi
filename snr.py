import numpy as np
import matplotlib.pyplot as plt

BIT_LEN = 16
MAX_BIT = (1 << BIT_LEN) - 1

x = np.logspace(1, np.log10(MAX_BIT), 100)
print(x)

print(x.astype("u8"))
y = x - (x + 0.5).astype("u8")
print(y)
