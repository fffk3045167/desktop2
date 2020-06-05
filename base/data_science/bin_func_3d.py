import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

x = np.arange(-4, 4, 0.01)
y = np.arange(-4, 4, 0.01)

# 把x,y数据生成mesh网格状的数据
x, y = np.meshgrid(x, y)

z = x - (1. / 9) * x ** 3 - (1. / 2) * y ** 2

# cmap是颜色映射表,可选：'rainbow',''coolwarm','blue'等
ax.plot_surface(x, y, z, cmap='rainbow')

plt.show()
