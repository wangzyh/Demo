# -*- coding:UTF-8 -*-
from threading import Thread, Lock
import time

g_num = 0

def test1():
    global g_num
    for i in range(1000000):
        # 上锁代码越少越好 而且还可以完成我们的任务
        mutex.acquire()
        g_num += 1
        mutex.release()

    print("---test1---g_num=%d"%g_num)

def test2():
    global g_num
    for i in range(1000000):
        # 通知
        mutex.acquire()
        g_num += 1
        mutex.release()

    print("---test2---g_num=%d"%g_num)

mutex = Lock()

p1 = Thread(target=test1)
p1.start()


p2 = Thread(target=test2)
p2.start()

print("---g_num=%d---"%g_num)

