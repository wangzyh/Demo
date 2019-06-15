from multiprocessing import Queue, Process
import random, time, os

#写数据进程执行的代码：
def write(q):
        for value in ["a","b","c"]:
            q.put(value)
            print("--%s已写入--"%value)
            time.sleep(random.random())
#读数据进程执行的代码
def read(q):
    while True:
        if not q.empty():
            value = q.get()
            print("---%s---"%value)
            time.sleep(random.random())
        else:
            break

if __name__=="__main__":
    # 父进程创建Queue，并传给各个子进程
    print("----1----")
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    #启动子进程pw，写入：
    pw.start()
    pw.join()
    # 启动子进程pr，读出：
    pr.start()
    pr.join()
    
    print("")
    print("所有数据输出完")
