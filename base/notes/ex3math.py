import matplotlib.pyplot as plt
import numpy as np
# fractions实现输出分数显示
from fractions import Fraction


def my_sum(*args):
    """求和"""
    result = 0
    for x in args:
        result += x
    return result


def my_power(x, n):
    """计算幂"""
    y = 1
    if type(n) is int:
        if n > 0:
            for i in range(n):
                y = y * x
            return y
        elif n == 0:
            return 1
        else:
            for i in range(-n):
                y = y * x
            return Fraction(1, y)
    else:
        print('ValueError!')


def my_sin(num):
    """绘制正弦函数图像"""
    x = np.linspace(0, 2 * np.pi)
    plt.plot(np.sin(num * x))
    plt.show()


def my_equal():
    """绘制饼图"""
    # test
    # a = [16065, 4998, 2802, 1484, 1076]
    # b = ["income", "traffic", "eat", "shopping", "live"]
    dataList = []
    dataLabel = []

    for i in range(3):
        dataLabel.append(input('way{}:'.format(i + 1)))
        dataList.append(int(input('money:')))

    plt.rcParams['font.sans-serif'] = ['KaiTi']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    plt.figure()
    plt.pie(dataList, labels=dataLabel, colors=["r", "y", "g", "b", "c", "m"], autopct="%1.2f%%")
    # 显示图例
    plt.legend()
    plt.title("年度消费\n总计：{}".format(np.sum(dataList)))
    # 将当前的图形变成圆形，默认为椭圆
    plt.axis("equal")

    plt.show()
