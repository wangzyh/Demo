from threading import Thread
import threading
import time

def test1():
    name = threading.current_thread().name
    print("---thread name is %s---"%name)
    g_num = 100
    if name == "Thread-1":
        g_num += 1
    else:
        time.sleep(2)
    print("---test1---g_num=%d"%g_num)

#def test2():
#    print("---test2---g_num=%d"%g_num)


p1 = Thread(target=test1)
p1.start()

p2 = Thread(target=test1)
p2.start()


