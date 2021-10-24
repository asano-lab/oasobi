import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)
# matplotlib.use("TkAgg")

x = np.linspace(0, 10, 100)
y = np.random.randn(100)
plt.plot(x, y)
plt.show()
