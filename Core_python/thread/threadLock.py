from atexit import register  # 使用atexit.register()函数来告知脚本何时结束
from random import randrange
from twisted.python.compat import xrange
from threading import Thread, currentThread
from time import ctime, sleep


class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)

# loops 是一个生成器
loops = (randrange(2,5) for x in xrange(randrange(3,7)))

remaining = CleanOutputSet()

def loop(nsec):
    my_name = currentThread().name
    remaining.add(my_name)
    print('[{}] Started {} '.format(ctime(), my_name))
    sleep(nsec)
    remaining.remove(my_name)
    print('[{}] Completed {} ({} secs)'.format(ctime(), my_name, nsec))
    print('(remaining: {})'.format(remaining or 'NONE'))

def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()


@register
def _atexit():
    print('all DONE at: ', ctime())

