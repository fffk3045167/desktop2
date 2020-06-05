from fractions import Fraction


def restrict(func):
    def num_is_true(x, n):
        """判断数据是否可用"""

        if type(x) is int and type(n) is int:
            if n > 0:
                return func(x, n)
            elif n == 0:
                return print('1')
            else:
                return func(Fraction(1, x), abs(n))
        else:
            print('ValueError!')
    return num_is_true


@restrict
def my_power(x, n):
    """计算幂"""
    s = 1
    for i in range(n):
        s = s * x
    print(s)


if __name__ == '__main__':
    my_power(2, -5)