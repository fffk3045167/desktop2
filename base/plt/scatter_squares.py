import matplotlib.pyplot as plt

x_values = list(range(1, 100))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
            edgecolors='none', s=40)
# 自动保存图表
plt.savefig('squares_plot.png', bbox_inches='tight')