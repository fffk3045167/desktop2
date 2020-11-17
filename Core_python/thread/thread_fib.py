from Core_python.thread.myThread import MyThread
from time import ctime, sleep

def fib(x):
    sleep(0.005)
    if x < 2:
        return 1
    return (fib(x-2) + fib(x-1))

def fac(x):
    sleep(0.1)
    if x < 2:
        return 1
    return (x * fac(x-1))

def sum(x):
    sleep(0.1)
    if x < 2:
        return 1
    return (x + sum(x-1))

funcs = [fib, fac, sum]
n = 12

def main():
    num_funcs = range(len(funcs))
    print('*** SINGLE THREAD')

    for i in num_funcs:
        print('starting', funcs[i].__name__, 'at: ', ctime())
        print(funcs[i](n))
        print(funcs[i].__name__, 'finished at: ', ctime())

    print('\n*** MULTIPLE THREADS')
    threads = []
    # Create threads
    for i in num_funcs:
        my_thread = MyThread(funcs[i], (n,), funcs[i].__name__)
        threads.append(my_thread)

    # Start threads
    for i in num_funcs:
        threads[i].start()

    # Wait until the thread is aborted
    for i in num_funcs:
        threads[i].join()
        print(threads[i].getResult())

    print('all DONE')


if __name__ == '__main__':
    main()