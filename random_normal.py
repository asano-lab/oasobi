import numpy as np
import matplotlib.pyplot as plt

nums = np.random.normal(12_310_100, 10000, 1000)
nums = nums.astype("int64")
print(nums.dtype)
print(nums)

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111)
ax.hist(nums)

plt.show()