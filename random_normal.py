import numpy as np
import matplotlib.pyplot as plt

a = np.random.normal(0.0, 1.0, 1000)
print(a)

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111)
ax.hist(a)

plt.show()