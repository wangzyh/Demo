from multiprocessing import Process
import time

def test():
    while True:
        print("---test---")
        time.sleep(1)

p = Process(target=test)
p.start() #让这个进程开始执行代码test函数中

while True:
    print("---main----")
    time.sleep(1)

