"""
# 包相对导入（导入当前目录下的模块）：使用号(.)，只能使用from语句
from ex3math import my_sum
from ex3math import my_power
from ex3math import my_sin
from ex3math import my_equal
import requests

print(my_sum(1, 2, 3, 4))

print(my_power(2, -5))

my_sin(0.25)

my_equal()

# 监视键盘和鼠标事件
for event in pygame.event.get():
    if event.type == pygame.OUIT:

# 分数类型
from fractions import Fraction

a = Fraction(4, 6)
b = Fraction("0.33")
print(a, b)

# 集合set
set1 = set([1, 3, 2, 8])
set2 = set("Hello")

# set1和set2的交集
a = set1 | set2
aa = set1.union(set2)

# 求差集（项在set1中, 但不在set2中）
b = set1 & set2
bb = set1.intersection(set2)

# 对称差集（项在set1或set2中, 但不会同时出现在二者中）
c = set1 ^ set2
cc = set1.symmetric_difference(set2)

print(set1, set2)
print(a, b, c)
print(aa, bb, cc)

# 增加、删除、更新set
set1.add(9)
set1.remove(3)
set1.update([11, 20, 13])

str1 = "  string object tea   "
a = str1.strip()
b = str1.lstrip()
print(a + 'aa')
print(b + 'aa')

import sys
print("my {1[spam]} runs {0.platform}".format(sys, {'spam': 'laptop'}))
print("first = {0[0]}, second = {0[1]}".format(['A', 'B', 'C']))


def func():
    '''function document'''
    print("func!")

# 输出注释文档
print(func.__doc__)
"""
import pyinstall
# 类的继承和子类的初始化


class FooParent(object):
    def __init__(self, a):
        self.parent = 'I\'m the Parent.'
        print('Parent:a=' + str(a))

    def bar(self, message):
        print(message + ' from Parent')


class FooChild(FooParent):
    def __init__(self, a):
        FooParent.__init__(self, a)
        print('Child:a=' + str(a))

    def bar(self, message):
        FooParent.bar(self, message)
        print(message + ' from Child')


fooChild = FooChild(10)
fooChild.bar('HelloWorld')
