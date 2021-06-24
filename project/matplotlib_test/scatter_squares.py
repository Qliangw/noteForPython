import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolors='none', s=40)

# plt.scatter(2, 4, s=20)

# 设置图标标题并给坐标轴加上标签
plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.axis([0, 1100, 0, 1100000])

# 设置刻度标记大小
# plt.tick_params(axis='both', which='major', labelsize=14)

# plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')

