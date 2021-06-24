import matplotlib.pyplot as plt
from random_walk import RandowWalkTest

while True:

    rw = RandowWalkTest(50000)
    rw.fill_walk()

    # 设置绘图窗口大小
    plt.figure(figsize=(10, 6))

    point_number = list(range(rw.num_points))

    plt.scatter(rw.x_values, rw.y_values,
                c=point_number, cmap=plt.cm.Blues,
                edgecolors='none', s=15)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=5)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=5)

    # 隐藏坐标轴
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    plt.axis('off')
    plt.savefig('rw_visual.png', bbox_inches='tight')
    # plt.show()

    keep_running = input("是否继续?(y/n):")
    if keep_running == 'n':
        break
