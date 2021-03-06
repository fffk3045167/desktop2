import threading
import time


exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print(self.name + "启动")
        print_time(self.name, self.counter, 5)
        print(self.name + "结束")

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s : %s " % (threadName, time.ctime(time.time())))
        counter -= 1

def main():
    # 创建线程
    thread1 = myThread(1, "Thread-1", 2)
    thread2 = myThread(2, "Thread-2", 4)

    # 开启新线程
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    print("结束主线程")

if __name__ == '__main__':
    main()