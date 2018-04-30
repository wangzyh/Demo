from multiprocessing import Manager, Pool
import random, time, os

#写数据进程执行的代码：
def read(q):
    print("write启动(%s),父进程为(%s)"%(os.getpid(),os.getppid()))
    for i in range(q.qsize()):
        print("reader从Queue获取到消息：%s"%q.get(True))

#读数据进程执行的代码
def write(q):
    print("write启动(%s),父进程为(%s)"%(os.getpid(),os.getppid()))
    for i in "dongGe":
        q.put(i)

if __name__=="__main__":
    # 父进程创建Queue，并传给各个子进程
    print("----1----")
    q = Manager().Queue()# 使用Manger中的Queue来初始化
    po = Pool()
    # 使用阻塞模式创建进程，这样就不需要在read中使用死循环了，可以让writer完全执行完成后，再用read
    po.apply(write, (q,))
    po.apply(read, (q,))
    
    po.close()
    po.join()

    print("(%s)End"%os.getpid())
    print("所有数据输出完")
