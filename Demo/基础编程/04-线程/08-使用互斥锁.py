# -*- coding:UTF-8 -*-
from threading import Thread, Lock
import time

g_num = 0

def test1():
    global g_num
    # 这个线程和test2线程都在抢着对 这个锁 进行上锁，如果有1方成功的上锁，那么导致另外一方会堵塞(一直等待) 到这个锁被解开为止
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    mutex.release()#用来对mutex指向的这个锁 进行解锁，，只要开了锁，那么接下来会让所有因为这个锁 被上了锁堵塞的线程进行抢着上锁

    print("---test1---g_num=%d"%g_num)

def test2():
    global g_num
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    mutex.release()

    print("---test2---g_num=%d"%g_num)

#创建一把互斥锁，默认没有上锁
mutex = Lock()

p1 = Thread(target=test1)
p1.start()

# time.sleep(3) #取消屏蔽之后 再次运行程序，结果会不一样，，，为啥呢？

p2 = Thread(target=test2)
p2.start()

print("---g_num=%d---"%g_num)

