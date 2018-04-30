from multiprocessing import Pool
import time
import os

def test1():
    print("----进程池中的进程----pid=%d,ppid=%d"%(os.getpid(),os.getppid()))
    for i in range(3):
        print("---%d---"%i)
        time.sleep(1)
    return "hahaha"

def test2(args):
    print("---callback func--pid=%d"%os.getpid())
    print("---callback func--args=%s"%args)

pool = Pool(3)
pool.apply_async(func=test1,callback=test2)

while True:
    time.sleep(1)
    print("---主进程-pid=%d---"%os.getpid())

