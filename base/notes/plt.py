import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(200).tolist()
y = np.random.rand(200).tolist()
size = np.random.rand(200).tolist() * 30
color = np.random.rand(200).tolist()
# print(type(x))
plt.scatter(x, y, size, color)
plt.colorbar()
plt.show()
