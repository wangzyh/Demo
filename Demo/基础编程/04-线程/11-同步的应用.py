from threading import Thread, Lock
import time


class Test1(Thread):
    def run(self):
        while True:
            if lock1.acquire():
                print("------Test1-----")
                time.sleep(0.5)
                lock2.release()


class Test2(Thread):
    def run(self):
        while True:
            if lock2.acquire():
                print("------Test2-----")
                time.sleep(0.5)
                lock3.release()


class Test3(Thread):
    def run(self):
        while True:
            if lock3.acquire():
                print("------Test3-----")
                time.sleep(0.5)
                lock1.release()


lock1 = Lock()

lock2 = Lock()
lock2.acquire()

lock3 = Lock()
lock3.acquire()

t1 = Test1()
t2 = Test2()
t3 = Test3()

t1.start()
t2.start()
t3.start()
