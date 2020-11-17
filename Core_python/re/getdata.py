from random import choice, randint
from string import ascii_lowercase as lc  # lowercase 所有小写字母字符串
from time import ctime


tlds = ('com', 'edu', 'net', 'org', 'gov')

with open('data.txt', 'a', encoding='utf-8') as f:
    for i in range(randint(5,10)):
        a = 630720000  # 1990年
        b = 1576800000  # 2020年
        year = randint(a, b)  # 1990-2020年之间
        #  ctime() 函数把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式
        dtstr = ctime(year)

        llen = randint(4, 7)
        # choice() 方法返回一个列表,元组或字符串的随机项
        # join 连接
        login = ''.join(choice(lc) for j in range(llen))
        dlen = randint(llen, 12)
        dom = ''.join(choice(lc) for j in range(dlen))

        # eval()执行一个字符串表达式，并返回表达式的值
        data = eval("'%s::%s@%s.%s::%d-%d-%d' % (dtstr, login, dom, choice(tlds), year, llen, dlen)")

        # 写入
        f.writelines(data + '\n')