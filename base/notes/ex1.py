PI = 3.1415926


def Sum(lst):
    tot = 0
    for value in lst:
        tot = tot + value
    return tot


w = [1, 2, 3, 4]
print(Sum(w), PI)
